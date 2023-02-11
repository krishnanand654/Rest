from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .serializers import EmployeeSerializer


class EmployeeLoginAPIView(generics.GenericAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("Email")
        password = request.data.get("Password")
        print(email)
        print(password)
        user = authenticate(request, Email=email, Password=password)
        if user:
            return Response({"message": "Login successful"})
        else:
            return Response({"message": "Invalid credentials"})
