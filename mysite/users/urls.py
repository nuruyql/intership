from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path('',include(router.urls)),

    path('register/',RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("profile/",ProfileView.as_view())
]


