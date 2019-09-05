from blog.models import Category, Post, Tag
from portfolio.models import Category

def blog_context(request):
    category = Category.objects.filter(is_draft=False)
    recent_post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:4]
    tag = Tag.objects.filter(is_draft=False)
    return {'category': category, 'r_post': recent_post, 'tag': tag}

def portfolio_context(request):
    category = Category.objects.filter(is_draft=False)
    return {'category': category}
