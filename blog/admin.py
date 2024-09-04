from django.contrib import admin

from .models import Featured, Tag, Category, Post, File


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "user", "created_at")


@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'icon', 'order']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'icon', 'order']



admin.site.register(File)