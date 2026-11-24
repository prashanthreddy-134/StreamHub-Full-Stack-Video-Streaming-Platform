from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ['name']; verbose_name_plural = 'Categories'
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self): return self.name

class Channel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='channel')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='channels/', blank=True, null=True)
    banner = models.ImageField(upload_to='channels/banners/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)[:100]
        super().save(*args, **kwargs)
    @property
    def subscriber_count(self): return self.subscribers.count()
    @property
    def total_views(self): return sum(v.views for v in self.videos.all())
    def __str__(self): return self.name

class Video(models.Model):
    STATUS_CHOICES = [('draft','Draft'),('published','Published'),('private','Private'),('unlisted','Unlisted')]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='videos')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='videos')
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    duration = models.PositiveIntegerField(default=0, help_text='Duration in seconds')
    views = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published')
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: ordering = ['-created_at']
    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:190] or 'video'
            candidate, n = base, 1
            while Video.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                n += 1; candidate = f'{base}-{n}'
            self.slug = candidate
        if self.status == 'published' and not self.published_at: self.published_at = timezone.now()
        super().save(*args, **kwargs)
    @property
    def like_count(self): return self.likes.filter(is_like=True).count()
    @property
    def dislike_count(self): return self.likes.filter(is_like=False).count()
    def __str__(self): return self.title

class Playlist(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='playlists')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class PlaylistVideo(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='items')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['order']; constraints = [models.UniqueConstraint(fields=['playlist','video'], name='unique_playlist_video')]

class Subscription(models.Model):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='subscribers')
    subscribed_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['subscriber','channel'], name='unique_user_channel_subscription')]

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ['-created_at']
    def __str__(self): return f'{self.user}: {self.content[:40]}'

class VideoView(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='view_logs')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

class VideoLike(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['video','user'], name='unique_user_video_reaction')]

class WatchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='watch_history')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now=True)
    watch_time = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['-watched_at']; constraints = [models.UniqueConstraint(fields=['user','video'], name='unique_user_watch_history')]
