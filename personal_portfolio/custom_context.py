from blog.models import PostCategory, Post, Tag
from portfolio.models import Category, Portfolio

def blog_context(request):
    post_category = PostCategory.objects.filter(is_draft=False)
    recent_post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:4]
    tag = Tag.objects.filter(is_draft=False)
    return {'post_category': post_category, 'r_post': recent_post, 'tag': tag}

def portfolio_context(request):
    portfolio_category = Category.objects.filter(is_draft=False)
    portfolio = Portfolio.objects.filter(is_draft=False)
    return {'portfolio_category': portfolio_category, 'portfolio': portfolio}
