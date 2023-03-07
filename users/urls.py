from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path(" ", ...),
    path(" ", ...),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
]