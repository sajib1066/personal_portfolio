from django.contrib import admin
from .models import Category, Portfolio

# admin customization
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'portfolio_type', 'category', 'is_draft', 'date']
    list_editable = ['title', 'portfolio_type', 'category', 'is_draft']
    list_filter = ('is_draft', 'portfolio_type')

# Register your models here.
admin.site.register(Category)
admin.site.register(Portfolio, PortfolioAdmin)
