from django.conf.urls import url, include
from .views import index, home_page

urlpatterns = [
    url(r'^$', index, name="index"),
]