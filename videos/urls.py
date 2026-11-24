from django.urls import path
from . import views
urlpatterns = [
 path('',views.home,name='home'), path('register/',views.register,name='register'),
 path('channel/create/',views.channel_setup,name='channel_setup'), path('my-channel/',views.my_channel,name='my_channel'),
 path('channel/<slug:slug>/',views.channel_detail,name='channel_detail'), path('upload/',views.upload_video,name='upload_video'),
 path('watch/<slug:slug>/',views.watch,name='watch'), path('watch/<slug:slug>/comment/',views.add_comment,name='add_comment'), path('watch/<slug:slug>/progress/',views.update_watch_time,name='update_watch_time'),
 path('watch/<slug:slug>/react/<str:kind>/',views.react,name='react'), path('channel/<slug:slug>/subscribe/',views.subscribe,name='subscribe'),
 path('playlists/',views.playlists,name='playlists'), path('playlists/<int:pk>/',views.playlist_detail,name='playlist_detail'),
 path('playlist/add/<int:video_id>/',views.add_to_playlist,name='add_to_playlist'), path('dashboard/',views.dashboard,name='dashboard'),
 path('history/',views.history,name='history'), path('video/<int:pk>/delete/',views.delete_video,name='delete_video'),
]
