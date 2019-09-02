from django.shortcuts import render
from .models import AuthorProfile, Category, Tag, Post


def blog_page(request):
    posts = Post.objects.filter(is_draft=False)
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def blog_details(request):
    return render(request, 'blog/single-blog.html')
