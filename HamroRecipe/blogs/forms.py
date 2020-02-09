from django import forms
from .models import Article


class BlogForm(forms.ModelForm):
    class Meta:
        username = forms.CharField()
        slug = forms.SlugField()
        body = forms.CharField()
        image = forms.ImageField()

