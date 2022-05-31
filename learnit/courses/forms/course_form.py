from django import forms

from courses.services.exceptions import PlaylistParseError
from courses.models import Course
from courses.services.playlist_parser_service import playlist_info

class CourseForm(forms.ModelForm):
    def clean_playlist_url(self):
        url = self.cleaned_data['playlist_url']
        try:
            playlist_info(url)
        except PlaylistParseError:
            raise forms.ValidationError('Playlist Parse Error')

        return  url


    class Meta:
        model = Course
        fields = [
            'category',
            'languare', 
            'priority', 
            'playlist_url', 
            'is_published'
            ]

