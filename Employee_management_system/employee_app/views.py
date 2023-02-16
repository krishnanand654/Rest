from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .serializers import EmployeeSerializer
from admin_app.models import LeaveApplication, EmployeeModel



class EmployeeList(generics.RetrieveAPIView):  # list  all employee
    lookup_field='pk'
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
