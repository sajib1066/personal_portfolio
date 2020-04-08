from django.shortcuts import render
from .models import AuthorProfile, PostCategory, Tag, Post


def blog_page(request):
    posts = Post.objects.filter(is_draft=False)
    context = {
        'posts': posts
    }
    return render(request, 'blog/post.html', context)

def blog_details(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/single-blog.html', context)

def search_post(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        post = Post.objects.filter(title__contains=keyword)
        context = {'post': post}
        return render(request, 'blog/search.html', context)
    return render(request, 'blog/search.html')

def blog_category_page(request, id):
    # ctg_id = PostCategory.objects.get(id=id)
    # print(ctg_id)
    post = Post.objects.filter(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/category-post.html', context)
