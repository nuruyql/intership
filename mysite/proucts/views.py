
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import SAFE_METHODS,BasePermission

from .serializers import *
from .models import *

# Create your views here.
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user and request.user.is_staff

class PhoneViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ["brand","model","description"]
    ordering_fields = ["price","created_at"]
    filterset_fields = ['category','stock']

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminOrReadOnly]


