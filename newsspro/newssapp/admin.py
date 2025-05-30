from django.contrib import admin
from .models import Category, Article, Bookmark

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'published_on', 'created_at']
    list_filter = ['category', 'published_on']
    search_fields = ['title', 'content']

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'article', 'created_at']
    list_filter = ['user', 'created_at']
    search_fields = ['article__title', 'user__username']
