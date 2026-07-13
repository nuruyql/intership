from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register("phones",PhoneViewSet)
router.register("category",CategoryViewSet)
router.register("favorite",FavoriteViewSet,basename="favorite"),
router.register("reviews",ReviewViewSet,basename="review")


urlpatterns =  [
    path("",include(router.urls)),
]