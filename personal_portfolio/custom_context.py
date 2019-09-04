from blog.models import Category

def category_list(request):
    category = Category.objects.filter(is_draft=False)
    return {'category': category}
