from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('faq.api.v1.urls'), name='v1'),
]
