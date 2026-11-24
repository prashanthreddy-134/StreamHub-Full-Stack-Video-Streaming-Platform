from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Video, Channel, Playlist, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta: model = User; fields = ('username','email','password1','password2')

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title','description','category','video_file','thumbnail','status')
        widgets = {'description': forms.Textarea(attrs={'rows':4})}
    def clean_video_file(self):
        f = self.cleaned_data['video_file']
        allowed = {'.mp4','.webm','.ogg','.mov'}
        import os
        if os.path.splitext(f.name)[1].lower() not in allowed: raise forms.ValidationError('Upload MP4, WebM, OGG or MOV video files only.')
        if f.size > 500 * 1024 * 1024: raise forms.ValidationError('Maximum video size is 500 MB.')
        return f
    def clean_thumbnail(self):
        f = self.cleaned_data.get('thumbnail')
        if f and f.size > 5 * 1024 * 1024: raise forms.ValidationError('Thumbnail must be 5 MB or smaller.')
        return f

class ChannelForm(forms.ModelForm):
    class Meta: model = Channel; fields = ('name','description','logo','banner')

class PlaylistForm(forms.ModelForm):
    class Meta: model = Playlist; fields = ('name','description','is_public')

class CommentForm(forms.ModelForm):
    class Meta: model = Comment; fields = ('content',); widgets = {'content': forms.Textarea(attrs={'rows':2,'placeholder':'Add a comment...'})}
