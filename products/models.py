from django.db.models import Avg
from django.db import models
from django.utils import timezone
import numpy as np
from django.contrib.auth.models import User



# Create your models here.


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
        
#    def average_rating(self):
#        all_ratings = map(lambda x: x.rating, self.rating_set.all())
#        return np.mean(all_ratings)

#    def average_rating(self):
#        Product.objects.all().aggregate(Avg('rating'))
        
#    def average_rating(self):
#        p = Product.objects.get('rating')
#        stars_average = p.rating_set.aggregate(Avg('rating'))
#        return stars_average

    def __str__(self):
        return self.name
        

# Review Model
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='review')
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
#   
    def average_rating(self):
       ratings = Review.objects.get('rating')
       stars_average = ratings.rating_set.aggregate(Avg('ratings'))
       return stars_average


    
