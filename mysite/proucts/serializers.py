from rest_framework import serializers
from .models import *
from django.db.models import Avg


class PhoneSerializers(serializers.ModelSerializer):

    average_rating = serializers.SerializerMethodField()

    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )
    class Meta:
        model = Phone
        fields = "__all__"
        read_only_fields = ["author"]

    def get_average_rating(self,obj):
            result = obj.reviews.aggregate(
                average= Avg("rating")
            )

            average = result["average"]

            if average is None:
                return 0
            return round(average , 1)

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


class ReviewSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ["user","created_at"]