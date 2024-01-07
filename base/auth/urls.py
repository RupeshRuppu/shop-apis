from django.urls import path
from .serializers import UserTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("token", UserTokenObtainPairView.as_view()),
    path("token/refresh", TokenRefreshView.as_view()),
]
