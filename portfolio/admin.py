from django.contrib import admin
from .models import Category, Portfolio

# admin customization
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_draft', 'date']
    list_editable = ['name', 'is_draft']

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'portfolio_type', 'category', 'is_draft', 'date']
    list_editable = ['title', 'portfolio_type', 'category', 'is_draft']
    list_filter = ('portfolio_type', 'is_draft')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
