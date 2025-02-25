from django.shortcuts import render
from .models import Task
from rest_framework import generics
from .serializers import TaskSerializer, RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validate the input data

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")

        user = authenticate(username = username, password = password )

        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                "refresh" : str(refresh),
                "access" : str(refresh.access_token),
                "user" : user_serializer.data,
            })
        else:
            return Response({"detail" : "Invalid Credentials"}, status=401)
        

class DashboardView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({
            "message" : "welcome to dashboard",
            "user" : user_serializer.data

        }, status=200)



# Task Views
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]  # Add authentication
    permission_classes = [IsAuthenticated]  # Require authenticated users
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)

class TasksRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

