from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_page, name='blog'),
    path('details/<int:post_id>', views.blog_details, name='blog-details'),
    path('search', views.search_post, name='search'),
    path('category/<int:id>', views.blog_category_page, name='category-post')
]
