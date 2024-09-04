from django.urls import path, include

urlpatterns = [
    path('api/v1/', include("users.api.v1.urls")),
]
