from django.urls import path

from .views import AuthorListView, AuthorTopListView

urlpatterns = [
    path('list/', AuthorListView.as_view(), name="author-list"),
    path('top/list/', AuthorTopListView.as_view(), name="author-top-list"),
]
