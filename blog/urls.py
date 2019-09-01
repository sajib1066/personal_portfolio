from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_page, name='blog'),
    path('details', views.blog_details, name='blog-details')
]
