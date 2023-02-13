
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
from .serializers import EmployeeCreateSerializer, EmployeeListSerializer, EmployeeDetailSerializer, LeaveListSerializer, LeaveApproveSerializer, UserSerializer

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class EmployeeCreate(generics.CreateAPIView, APIView):  # create employee
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeCreateSerializer

    # # permission_classes = [IsAdminUser, IsAuthenticated]

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
    # permission_classes = [IsAdminUser, IsAuthenticated]


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


class LeaveList(generics.ListAPIView):  # list  all employee
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveListSerializer
    # permission_classes = [IsAdminUser, IsAuthenticated]


class LeaveApprove(generics.RetrieveUpdateAPIView):  # list  all employee

    parser_classes = (MultiPartParser, JSONParser)
    lookup_field = 'emp_id'
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApproveSerializer

    def get_object(self):
        id = self.kwargs.get(self.lookup_field)
        l_id = self.kwargs.get('leaveid')
        if l_id is not None:
            return get_object_or_404(self.queryset, emp_id=id, id=l_id)
        else:
            return get_object_or_404(self.queryset, emp_id=id)

        # return get_object_or_404(self.queryset, emp_id=id)


class ApprovedLeavesList(generics.ListAPIView):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveListSerializer
    # permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        status = self.kwargs.get('status')
        if status == 'approved':
            return self.queryset.filter(status='approved')
        elif status == 'pending':
            return self.queryset.filter(status='pending')


class SortedEmployeeView(generics.ListAPIView):
    serializer_class = EmployeeListSerializer

    def get_queryset(self):
        sort = self.kwargs.get('sort')
        if sort == 'asc':
            return EmployeeModel.objects.all().order_by('Employee_Id')
        elif sort == 'desc':
            return EmployeeModel.objects.all().order_by('-Employee_Id')
        else:
            queryset = EmployeeModel.objects.all()
        return queryset


class SearchEmployeeView(generics.ListAPIView):
    serializer_class = EmployeeListSerializer

    def get_queryset(self):
        emp_id = self.kwargs['emp_id']
        return EmployeeModel.objects.filter(Employee_Id=emp_id)


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
