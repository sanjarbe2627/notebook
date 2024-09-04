from rest_framework import serializers

from users.models import User


class AuthorSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'pk', 'first_name', 'last_name', 'email', 'post_count',
            'avatar', 'instagram', 'twitter', 'facebook', 'date_joined'
        ]

    def get_post_count(self, obj):
        return obj.posts.count()
