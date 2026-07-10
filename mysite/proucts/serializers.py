from rest_framework import serializers
from .models import *


class PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"