from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register("phones",PhoneViewSet)
router.register("category",CategoryViewSet)


urlpatterns =  [
    path("",include(router.urls)),
]