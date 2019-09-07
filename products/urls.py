from django.conf.urls import url, include
from .views import all_products, product_detail, add_review_to_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
#    url(r'^$', views.review_list, name='review_list'),
#    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
]