from rest_framework import serializers

from users.api.v1.serializers import AuthorSerializer
from ...models import Post, Featured, Tag, Category, File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['pk', 'file', 'created_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["pk", "title"]


class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ['pk', 'title', 'icon', 'post_count']

    def get_post_count(self, obj):
        return obj.posts.count()


class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = ['pk', 'icon', 'title', 'order']


class PostSerializer(serializers.ModelSerializer):
    images = FileSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    user = AuthorSerializer(many=False, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['pk', 'title', 'category', 'user', 'images', 'description', 'tags', 'created_at', 'updated_at']


class PostListSerializer(PostSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        return obj.description[:30] + "...." if len(obj.description) > 30 else obj.description
