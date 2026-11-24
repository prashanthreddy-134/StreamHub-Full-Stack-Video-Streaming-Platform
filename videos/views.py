
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum, F
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.utils.text import slugify

from .forms import (
    RegisterForm,
    VideoForm,
    ChannelForm,
    PlaylistForm,
    CommentForm,
)

from .models import (
    Category,
    Channel,
    Video,
    Playlist,
    PlaylistVideo,
    Subscription,
    Comment,
    VideoView,
    VideoLike,
    WatchHistory,
)


# --------------------------------------------------
# HOME PAGE AND VIDEO SEARCH
# --------------------------------------------------

def home(request):
    videos = (
        Video.objects
        .filter(status='published')
        .select_related('channel', 'category')
    )

    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '')

    if query:
        videos = videos.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(channel__name__icontains=query)
        )

    if category:
        videos = videos.filter(category__slug=category)

    return render(request, 'videos/home.html', {
        'videos': videos,
        'categories': Category.objects.all(),
        'active_category': category,
        'query': query,
    })


# --------------------------------------------------
# USER REGISTRATION
# --------------------------------------------------

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                'Your account is ready. Create your channel to start uploading.'
            )

            return redirect('channel_setup')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {
        'form': form,
    })


# --------------------------------------------------
# CHANNEL CREATION
# --------------------------------------------------

@login_required
def channel_setup(request):
    if hasattr(request.user, 'channel'):
        return redirect('my_channel')

    if request.method == 'POST':
        form = ChannelForm(request.POST, request.FILES)

        if form.is_valid():
            channel = form.save(commit=False)
            channel.user = request.user
            channel.slug = slugify(form.cleaned_data['name'])

            if Channel.objects.filter(slug=channel.slug).exists():
                channel.slug = f'{channel.slug}-{request.user.id}'

            channel.save()

            messages.success(request, 'Channel created successfully.')

            return redirect('my_channel')
    else:
        form = ChannelForm()

    return render(request, 'videos/form_page.html', {
        'form': form,
        'heading': 'Create your channel',
        'button': 'Create channel',
    })


@login_required
def my_channel(request):
    channel = getattr(request.user, 'channel', None)

    if not channel:
        return redirect('channel_setup')

    return render(request, 'videos/channel.html', {
        'channel': channel,
        'is_owner': True,
        'is_subscribed': False,
    })


def channel_detail(request, slug):
    channel = get_object_or_404(Channel, slug=slug)

    is_owner = (
        request.user.is_authenticated
        and request.user == channel.user
    )

    is_subscribed = False

    if request.user.is_authenticated and not is_owner:
        is_subscribed = Subscription.objects.filter(
            channel=channel,
            subscriber=request.user
        ).exists()

    return render(request, 'videos/channel.html', {
        'channel': channel,
        'is_owner': is_owner,
        'is_subscribed': is_subscribed,
    })


# --------------------------------------------------
# VIDEO UPLOAD
# --------------------------------------------------

@login_required
def upload_video(request):
    channel = getattr(request.user, 'channel', None)

    if not channel:
        messages.info(
            request,
            'Create a channel before uploading videos.'
        )
        return redirect('channel_setup')

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():
            video = form.save(commit=False)
            video.channel = channel
            video.save()

            messages.success(
                request,
                'Video uploaded successfully.'
            )

            return redirect('watch', slug=video.slug)
    else:
        form = VideoForm()

    return render(request, 'videos/form_page.html', {
        'form': form,
        'heading': 'Upload a video',
        'button': 'Publish video',
    })


# --------------------------------------------------
# VIDEO WATCH PAGE
# --------------------------------------------------

def watch(request, slug):
    video = get_object_or_404(
        Video.objects.select_related('channel', 'category'),
        slug=slug
    )

    is_owner = (
        request.user.is_authenticated
        and request.user == video.channel.user
    )

    if video.status == 'private' and not is_owner:
        return HttpResponseForbidden('This video is private.')

    if video.status == 'draft' and not is_owner:
        return HttpResponseForbidden('This video is not published.')

    ip = request.META.get('REMOTE_ADDR')

    VideoView.objects.create(
        video=video,
        user=request.user if request.user.is_authenticated else None,
        ip_address=ip,
        user_agent=request.META.get('HTTP_USER_AGENT', '')[:255],
    )

    Video.objects.filter(pk=video.pk).update(
        views=F('views') + 1
    )

    if request.user.is_authenticated:
        WatchHistory.objects.get_or_create(
            user=request.user,
            video=video,
            defaults={'watch_time': 0}
        )

    related = (
        Video.objects
        .filter(status='published')
        .exclude(pk=video.pk)
    )

    if video.category_id:
        related = related.filter(category=video.category)

    user_reaction = None
    is_subscribed = False
    user_playlists = Playlist.objects.none()

    if request.user.is_authenticated:
        user_reaction = VideoLike.objects.filter(
            video=video,
            user=request.user
        ).first()

        is_subscribed = Subscription.objects.filter(
            channel=video.channel,
            subscriber=request.user
        ).exists()

        user_channel = getattr(request.user, 'channel', None)

        if user_channel:
            user_playlists = Playlist.objects.filter(
                channel=user_channel
            )

    return render(request, 'videos/watch.html', {
        'video': video,
        'comment_form': CommentForm(),
        'comments': video.comments.filter(
            parent__isnull=True
        ).select_related('user'),
        'related': related[:5],
        'user_reaction': user_reaction,
        'is_subscribed': is_subscribed,
        'is_owner': is_owner,
        'user_playlists': user_playlists,
    })


# --------------------------------------------------
# COMMENTS
# --------------------------------------------------

@login_required
@require_POST
def add_comment(request, slug):
    video = get_object_or_404(
        Video,
        slug=slug,
        status='published'
    )

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.video = video
        comment.user = request.user
        comment.save()

        messages.success(request, 'Comment added successfully.')
    else:
        messages.error(request, 'Please enter a valid comment.')

    return redirect('watch', slug=slug)


# --------------------------------------------------
# LIKE AND DISLIKE
# --------------------------------------------------

@login_required
@require_POST
def react(request, slug, kind):
    if kind not in ('like', 'dislike'):
        return redirect('watch', slug=slug)

    video = get_object_or_404(
        Video,
        slug=slug,
        status='published'
    )

    is_like = kind == 'like'

    reaction = VideoLike.objects.filter(
        video=video,
        user=request.user
    ).first()

    if reaction and reaction.is_like == is_like:
        reaction.delete()
    else:
        VideoLike.objects.update_or_create(
            video=video,
            user=request.user,
            defaults={'is_like': is_like}
        )

    return redirect('watch', slug=slug)


# --------------------------------------------------
# SUBSCRIBE AND UNSUBSCRIBE
# --------------------------------------------------

@login_required
@require_POST
def subscribe(request, slug):
    channel = get_object_or_404(
        Channel,
        slug=slug
    )

    if channel.user_id == request.user.id:
        messages.warning(
            request,
            'You cannot subscribe to your own channel.'
        )
    else:
        subscription = Subscription.objects.filter(
            channel=channel,
            subscriber=request.user
        )

        if subscription.exists():
            subscription.delete()

            messages.info(
                request,
                'Subscription removed.'
            )
        else:
            Subscription.objects.create(
                channel=channel,
                subscriber=request.user
            )

            messages.success(
                request,
                'Subscribed to channel.'
            )

    return redirect('channel_detail', slug=slug)


# --------------------------------------------------
# PLAYLIST MANAGEMENT
# --------------------------------------------------

@login_required
def playlists(request):
    channel = getattr(request.user, 'channel', None)

    if not channel:
        messages.info(
            request,
            'Create your channel before creating playlists.'
        )
        return redirect('channel_setup')

    if request.method == 'POST':
        form = PlaylistForm(request.POST)

        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.channel = channel
            playlist.save()

            messages.success(
                request,
                'Playlist created successfully.'
            )

            return redirect('playlists')
    else:
        form = PlaylistForm()

    # Show published videos from all creators.
    videos = (
        Video.objects
        .filter(status='published')
        .select_related('channel', 'category')
    )

    return render(request, 'videos/playlists.html', {
        'playlists': channel.playlists.all(),
        'form': form,
        'channel': channel,
        'videos': videos,
    })


# --------------------------------------------------
# ADD VIDEO TO PLAYLIST
# --------------------------------------------------

@login_required
@require_POST
def add_to_playlist(request, video_id):
    # Allow saving published videos from any creator.
    video = get_object_or_404(
        Video,
        pk=video_id,
        status='published'
    )

    channel = getattr(request.user, 'channel', None)

    if not channel:
        messages.error(
            request,
            'Create your channel before saving videos to playlists.'
        )
        return redirect('channel_setup')

    # A user can only add videos to their own playlists.
    playlist = get_object_or_404(
        Playlist,
        pk=request.POST.get('playlist'),
        channel=channel
    )

    # Avoid adding the same video more than once.
    PlaylistVideo.objects.get_or_create(
        playlist=playlist,
        video=video,
        defaults={
            'order': playlist.items.count()
        }
    )

    messages.success(
        request,
        f'"{video.title}" added to "{playlist.name}".'
    )

    return redirect('playlist_detail', pk=playlist.pk)


# --------------------------------------------------
# PLAYLIST DETAIL
# --------------------------------------------------

def playlist_detail(request, pk):
    playlist = get_object_or_404(
        Playlist.objects.select_related('channel'),
        pk=pk
    )

    if not playlist.is_public:
        if (
            not request.user.is_authenticated
            or request.user != playlist.channel.user
        ):
            return HttpResponseForbidden(
                'This playlist is private.'
            )

    return render(request, 'videos/playlist_detail.html', {
        'playlist': playlist,
    })


# --------------------------------------------------
# CREATOR DASHBOARD
# --------------------------------------------------

@login_required
def dashboard(request):
    channel = getattr(request.user, 'channel', None)

    if not channel:
        return redirect('channel_setup')

    videos = channel.videos.all()

    return render(request, 'videos/dashboard.html', {
        'channel': channel,
        'videos': videos,
        'total_views': videos.aggregate(
            total=Sum('views')
        )['total'] or 0,
        'total_likes': VideoLike.objects.filter(
            video__channel=channel,
            is_like=True
        ).count(),
        'total_comments': Comment.objects.filter(
            video__channel=channel
        ).count(),
    })


# --------------------------------------------------
# WATCH HISTORY
# --------------------------------------------------

@login_required
def history(request):
    return render(request, 'videos/history.html', {
        'history': (
            WatchHistory.objects
            .filter(user=request.user)
            .select_related('video', 'video__channel')
        )
    })


# --------------------------------------------------
# DELETE VIDEO
# --------------------------------------------------

@login_required
@require_POST
def delete_video(request, pk):
    video = get_object_or_404(
        Video,
        pk=pk,
        channel__user=request.user
    )

    video.delete()

    messages.success(
        request,
        'Video deleted successfully.'
    )

    return redirect('dashboard')


# --------------------------------------------------
# WATCH PROGRESS TRACKING
# --------------------------------------------------

@login_required
@require_POST
def update_watch_time(request, slug):
    video = get_object_or_404(
        Video,
        slug=slug
    )

    try:
        seconds = max(
            0,
            min(
                int(request.POST.get('seconds', '0')),
                86400
            )
        )
    except (TypeError, ValueError):
        return JsonResponse(
            {'error': 'Invalid watch time'},
            status=400
        )

    history, created = WatchHistory.objects.get_or_create(
        user=request.user,
        video=video,
        defaults={
            'watch_time': seconds
        }
    )

    if not created and seconds > history.watch_time:
        history.watch_time = seconds
        history.save(
            update_fields=['watch_time', 'watched_at']
        )

    return JsonResponse({
        'ok': True,
        'watch_time': history.watch_time,
    })
