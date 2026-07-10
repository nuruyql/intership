from rest_framework import serializers
from .models import *


class PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"
        read_only_fields = ["author"]

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FavoriteSerializers(serializers.ModelSerializer):
    user  = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Favorite
        fields = "__all__"
        read_only_fields = ["user","created_at"]