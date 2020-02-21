from django import forms

from .models import Post, Clue

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ClueForm(forms.ModelForm):

    class Meta:
        model = Clue
        fields = ('text', 'length')

        