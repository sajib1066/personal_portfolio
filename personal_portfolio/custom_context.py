from blog.models import Category, Post, Tag

def category_list(request):
    category = Category.objects.filter(is_draft=False)
    recent_post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:4]
    tag = Tag.objects.filter(is_draft=False)
    return {'category': category, 'r_post': recent_post, 'tag': tag}
