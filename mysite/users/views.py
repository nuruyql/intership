from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import *



# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers 
    permission_classes = [AllowAny]


class ProfileView(RetrieveAPIView):
    serializer_class = ProfilSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
