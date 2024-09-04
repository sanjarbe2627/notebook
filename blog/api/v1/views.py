from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ...models import Tag, Category, Featured, Post
from base.utils.pagination import CustomPagination
from .serializers import TagSerializer, CategorySerializer, FeaturedSerializer, PostListSerializer, PostSerializer


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


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset

        title = self.request.query_params.get('title')
        category = self.request.query_params.get('category')
        tag = self.request.query_params.get('tag')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if category:
            queryset = queryset.filter(category__pk=category)
        if tag:
            queryset = queryset.filter(tags__pk__in=tag.split(','))

        return queryset


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = Post.objects.get(pk=kwargs.get("pk"))
        except Post.DoesNotExist:
            return Response({}, status=status.HTTP_200_OK)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
