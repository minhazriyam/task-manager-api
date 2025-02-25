from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {
        "password": {"write_only": True}  
        }


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required= True)
    password = serializers.CharField(required= True, write_only = True)




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'user', 'status']
