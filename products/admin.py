from django.contrib import admin
from .models import Product, Review

# Register your models here.
admin.site.register(Product)

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('product', 'rating', 'user_name', 'comment', 'published_date')
    list_filter = ['published_date', 'user_name']
    search_fields = ['comment']
    
admin.site.register(Review, ReviewAdmin)