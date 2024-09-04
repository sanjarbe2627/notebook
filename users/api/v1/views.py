from django.db.models import Count
from rest_framework import generics

from base.utils.pagination import CustomPagination
from .serializers import AuthorSerializer

from ...models import User


class AuthorListView(generics.ListAPIView):
    queryset = User.objects.filter(is_verified=True, is_active=True)
    serializer_class = AuthorSerializer
    pagination_class = CustomPagination


class AuthorTopListView(generics.ListAPIView):
    queryset = User.objects.annotate(
        count=Count('posts')).filter(is_verified=True, is_active=True).order_by('-count')[:10]
    serializer_class = AuthorSerializer
    pagination_class = CustomPagination
