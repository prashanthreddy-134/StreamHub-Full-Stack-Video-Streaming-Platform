from django.contrib import admin
from .models import Category,Channel,Video,Playlist,PlaylistVideo,Subscription,Comment,VideoView,VideoLike,WatchHistory
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): list_display=('name','slug','created_at'); prepopulated_fields={'slug':('name',)}
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin): list_display=('name','user','created_at'); search_fields=('name','user__username')
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin): list_display=('title','channel','category','status','views','created_at'); list_filter=('status','category'); search_fields=('title','channel__name'); readonly_fields=('views','created_at','updated_at')
admin.site.register([Playlist,PlaylistVideo,Subscription,Comment,VideoView,VideoLike,WatchHistory])
admin.site.site_header='StreamHub Administration'
admin.site.site_title='StreamHub Admin'
admin.site.index_title='Platform management'
