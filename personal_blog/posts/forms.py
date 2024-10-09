from django import forms
from django.forms import ModelForm

from .models import Post

class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['heading', 'text', 'image']
        widgets = {
            'heading': forms.TextInput(attrs={'class': 'create-form-input'}),
            'text': forms.Textarea(attrs={'class': 'create-form-input'}),
        }

        labels = {
            "heading": 'Title',
            'text': 'Opinion'
        }
    # image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'create-form-img-label'}))


