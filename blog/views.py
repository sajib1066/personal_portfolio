from django.shortcuts import render


def blog_page(request):
    return render(request, 'blog/blog.html')

def blog_details(request):
    return render(request, 'blog/single-blog.html')
