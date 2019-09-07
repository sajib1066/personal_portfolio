from django.contrib import admin
from . import models

# admin customization
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'gender', 'date']
    list_filter = ('gender',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'is_draft', 'date']
    list_editable = ['name', 'author', 'is_draft']
    list_filter = ('author', )

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'is_draft', 'date']
    list_editable = ['name', 'author', 'is_draft']
    list_filter = ('author', )

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'author', 'is_draft', 'pub_date']
    list_editable = ['title', 'category', 'is_draft']
    list_filter = ('category', 'author', 'is_draft')

# Register your models here.

admin.site.register(models.AuthorProfile, AuthorProfileAdmin)
admin.site.register(models.PostCategory, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Post, PostAdmin)
