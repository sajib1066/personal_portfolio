from django.shortcuts import render
from blog.models import Post

def home_page(request):
    post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:3]
    context = {'post': post}
    return render(request, 'home.html', context)

def about_page(request):
    return render(request, 'about.html')

def service_page(request):
    return render(request, 'services.html')

def contact_page(request):
    return render(request, 'contact.html')
