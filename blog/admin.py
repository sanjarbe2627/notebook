from django.contrib import admin

from .models import Featured, Tag, Category


@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'icon', 'order']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'icon', 'order']
