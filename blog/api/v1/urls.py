from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagViewSets, CategoryViewSet, FeaturedViewSet, PostListView, PostDetailView

router = DefaultRouter()
router.register(r'tags', TagViewSets, basename='tags')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'featured', FeaturedViewSet, basename='featured')

urlpatterns = [
    path('post/list/', PostListView.as_view(), name='post-list'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', include(router.urls)),
]
