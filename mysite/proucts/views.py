
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly,IsReviewOwnerOrReadOnly
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PhoneViewSet(ModelViewSet):
    queryset = Phone.objects.select_related("category")
    serializer_class = PhoneSerializers
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    permission_classes = [IsOwnerOrReadOnly]
    search_fields = ["brand","model","description"]
    ordering_fields = ["price","created_at"]
    filterset_fields = ['category','stock']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminOrReadOnly]


class FavoriteViewSet(ModelViewSet):
    serializer_class = FavoriteSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class=ReviewSerializers
    permission_classes = [IsReviewOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["phone","rating"]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)