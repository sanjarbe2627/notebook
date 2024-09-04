from rest_framework import serializers

from users.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'email', 'avatar', 'instagram', 'twitter', 'facebook', 'date_joined']
