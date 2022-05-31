from attr import fields
from django import forms

from courses.models import ImageStyle

class ImageStyleForm(forms.ModelForm):
    class Meta:
        model = ImageStyle
        fields = [
            'name',
            'bg_color',
            'title_color',
            'watemark',
            'watemark_color',
        ]