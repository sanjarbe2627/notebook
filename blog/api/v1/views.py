from rest_framework import viewsets

from ...models import Tag, Category, Featured
from base.utils.pagination import CustomPagination
from .serializers import TagSerializer, CategorySerializer, FeaturedSerializer


class TagViewSets(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = CustomPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination

class FeaturedViewSet(viewsets.ModelViewSet):
    queryset = Featured.objects.all()
    serializer_class = FeaturedSerializer
    pagination_class = CustomPagination
