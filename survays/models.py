from django.db import models
from django.utils import timezone

# Create your models here.

class FirstSurvay(models.Model):
    """
    A single survay 
    """
#    author = models.ForeignKey(get_user_model(), null=True)     
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    category = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=255, null=True)