from django import forms
from .models import Post,Comment,Reply
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author","post_type",)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
