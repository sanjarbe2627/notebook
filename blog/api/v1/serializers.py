from rest_framework import serializers

from django.contrib.auth.models import User
from ...models import Post, Featured, Tag, Category, File


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["pk", "title"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'title', 'icon']


class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = ['pk', 'icon', 'title', 'order']
