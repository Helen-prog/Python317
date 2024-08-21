from django import forms

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
