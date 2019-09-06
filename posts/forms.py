from django import forms
from .models import Post, Comment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'content', 'image', 'tag', 'published_date',
        'category', 'location')
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')