from django.contrib.auth.models import User
from rest_framework import serializers



class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ["id","username","password"]

    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        return user 

class ProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username"]