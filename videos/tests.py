from django.test import TestCase, Client, override_settings
from tempfile import gettempdir
import os
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import Category, Channel, Video, Subscription, VideoLike, Comment, Playlist, PlaylistVideo

@override_settings(MEDIA_ROOT=os.path.join(gettempdir(), 'streamhub-test-media'))
class PlatformTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='creator',password='TestPass123!')
        self.viewer=User.objects.create_user(username='viewer',password='TestPass123!')
        self.channel=Channel.objects.create(user=self.user,name='Creator Channel')
        self.category=Category.objects.create(name='Technology')
        self.video=Video.objects.create(title='Django Basics',description='A test video',channel=self.channel,category=self.category,video_file=SimpleUploadedFile('sample.mp4',b'fake-video-content',content_type='video/mp4'))
        self.client=Client()

    def test_homepage_loads(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Django Basics')

    def test_video_watch_page_loads_and_tracks_view(self):
        response=self.client.get(reverse('watch',args=[self.video.slug]))
        self.assertEqual(response.status_code,200)
        self.video.refresh_from_db()
        self.assertEqual(self.video.views,1)
        self.assertEqual(self.video.view_logs.count(),1)

    def test_registration_page_loads(self):
        self.assertEqual(self.client.get(reverse('register')).status_code,200)

    def test_login_and_dashboard_access(self):
        self.client.login(username='creator',password='TestPass123!')
        response=self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Creator Channel')

    def test_subscribe_and_unsubscribe(self):
        self.client.login(username='viewer',password='TestPass123!')
        url=reverse('subscribe',args=[self.channel.slug])
        self.client.post(url)
        self.assertTrue(Subscription.objects.filter(subscriber=self.viewer,channel=self.channel).exists())
        self.client.post(url)
        self.assertFalse(Subscription.objects.filter(subscriber=self.viewer,channel=self.channel).exists())

    def test_like_toggle(self):
        self.client.login(username='viewer',password='TestPass123!')
        url=reverse('react',args=[self.video.slug,'like'])
        self.client.post(url)
        self.assertTrue(VideoLike.objects.filter(user=self.viewer,video=self.video,is_like=True).exists())
        self.client.post(url)
        self.assertFalse(VideoLike.objects.filter(user=self.viewer,video=self.video).exists())

    def test_comment_submission(self):
        self.client.login(username='viewer',password='TestPass123!')
        self.client.post(reverse('add_comment',args=[self.video.slug]),{'content':'Great tutorial'})
        self.assertTrue(Comment.objects.filter(video=self.video,user=self.viewer,content='Great tutorial').exists())

    def test_playlist_creation(self):
        self.client.login(username='creator',password='TestPass123!')
        response=self.client.post(reverse('playlists'),{'name':'Learning Python','description':'Course videos','is_public':'on'})
        self.assertEqual(response.status_code,302)
        self.assertTrue(Playlist.objects.filter(channel=self.channel,name='Learning Python').exists())

    def test_private_video_restricted(self):
        self.video.status='private'; self.video.save()
        response=self.client.get(reverse('watch',args=[self.video.slug]))
        self.assertEqual(response.status_code,403)


    def test_watch_time_progress_endpoint(self):
        self.client.login(username='viewer',password='TestPass123!')
        self.client.post(reverse('watch',args=[self.video.slug]))
        response=self.client.post(reverse('update_watch_time',args=[self.video.slug]),{'seconds':'42'})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json()['watch_time'],42)

    def test_playlist_add_video(self):
        playlist=Playlist.objects.create(channel=self.channel,name='My playlist')
        self.client.login(username='creator',password='TestPass123!')
        response=self.client.post(reverse('add_to_playlist',args=[self.video.pk]),{'playlist':playlist.pk})
        self.assertEqual(response.status_code,302)
        self.assertTrue(PlaylistVideo.objects.filter(playlist=playlist,video=self.video).exists())

    def test_search_filters_video(self):
        response=self.client.get(reverse('home'),{'q':'Django'})
        self.assertContains(response,'Django Basics')
        response=self.client.get(reverse('home'),{'q':'not-a-match'})
        self.assertNotContains(response,'Django Basics')
