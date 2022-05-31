from attr import fields
from django import forms

from courses.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'parent_category',
            'name',
            'image_style',
            'priority',
            'languare',
            'is_published',
        ]