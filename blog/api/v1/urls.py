from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagViewSets, CategoryViewSet, FeaturedViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSets, basename='tags')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'featured', FeaturedViewSet, basename='featured')

urlpatterns = [
    path('', include(router.urls)),
]
