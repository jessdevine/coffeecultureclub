from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model





class Post(models.Model):
    """
    A single Blog post
    """
#    author = models.ForeignKey(get_user_model(), null=True)     
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    category = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=255, null=True)
    
    
    def __unicode__(self):
        return self.title

        
class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    attending = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text