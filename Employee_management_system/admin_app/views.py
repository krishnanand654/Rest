
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from django.shortcuts import render
from rest_framework.parsers import JSONParser, MultiPartParser
from .models import EmployeeModel, LeaveApplication
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeCreateSerializer, EmployeeListSerializer, EmployeeDetailSerializer, LeaveDetailSerializer, LeaveCreateSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class EmployeeCreate(generics.CreateAPIView, APIView):  # create employee
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeCreateSerializer

    permission_classes = [IsAdminUser, IsAuthenticated]

    # permission_classes = [IsAuthenticated]
    # parser_classes = (MultiPartParser, JSONParser)


class EmployeeList(generics.ListAPIView):  # list  all employee
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeListSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class EmployeeDetail(generics.RetrieveAPIView):
    lookup_field = 'pk'  # details of particular employee
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class EmployeeUpdateDetail(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'  # details of particular employee
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class EmployeeDeleteDetail(generics.RetrieveDestroyAPIView):
    lookup_field = 'pk'
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeCreateSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class LeaveDetail(generics.RetrieveAPIView):
    lookup_field = 'pk'  # details of particular employee
    print(EmployeeModel.objects.values('Email'))
    queryset = EmployeeModel.objects.values('Email')
    serializer_class = LeaveDetailSerializer


class LeaveCreate(generics.ListCreateAPIView, APIView):
    lookup_field = 'pk'  # create employee
    queryset = EmployeeModel.objects.values('Email')
    queryset = LeaveApplication.objects.all()


class LeaveView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    queryset = LeaveApplication.objects.values('user')
    serializer_class = LeaveCreateSerializer

# class LoginView(generics.CreateAPIView):
#     serializer_class = UserSerializer

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email", "")
#         password = request.data.get("password", "")
#         user = EmployeeModel.objects.filter(Email=email).first()
#         if user is not None:
#             authenticated_user = authenticate(
#                 Username=user.Email, Password=password)
#             if authenticated_user is not None:
#                 login(request, authenticated_user)
#                 return Response({"message": "User authenticated successfully"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)


# class LogoutView(generics.CreateAPIView):
#     authentication_classes = [JWTAuthentication]

#     def post(self, request, *args, **kwargs):
#         try:
#             request.user.auth_token.delete()
#         except (AttributeError, ObjectDoesNotExist):
#             return Response({"error": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"message": "Token deleted successfully"}, status=status.HTTP_200_OK)
