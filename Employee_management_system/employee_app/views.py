from rest_framework.decorators import permission_classes, authentication_classes,  renderer_classes
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
# from rest_framework import exceptions
from rest_framework import authentication
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render
from admin_app.models import EmployeeModel, LeaveApplication

from rest_framework.permissions import IsAuthenticated

from .serializers import LeaveApplicationSerializer, UserSerializer
from rest_framework import status


# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import authentication






class ObtainAuthTokenView(generics.GenericAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'})


class LeaveView(generics.RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'emp_id'  # details of particular employee
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.id != self.kwargs.get(self.lookup_field):
            return Response({"error": "Unauthorized Access"}, status=status.HTTP_401_UNAUTHORIZED)
        id = self.kwargs.get(self.lookup_field)
        leave_data = self.queryset.filter(user=id)
        serializer = LeaveApplicationSerializer(leave_data, many=True)
        return Response(serializer.data)

    def post(self, request, emp_id):
        user = request.user
        if user.id != emp_id:
            return Response({"error": "Unauthorized Access"}, status=status.HTTP_401_UNAUTHORIZED)

        employee = EmployeeModel.objects.get(user=emp_id)

        emp_id = employee.user.id
        emp_name = employee.Employee_Name

        leave = LeaveApplication.objects.create(
            user=employee,
            emp_id=emp_id,
            emp_name=emp_name,

            apply_date=request.data.get('apply_date'),
            nature_of_leave=request.data.get('nature_of_leave'),
            first_Day=request.data.get('first_Day'),
            last_Day=request.data.get('last_Day'),
            number_Of_Days=request.data.get('number_Of_Days'),

        )

        return Response({'status': 'Leave request created'})

    def save(self, *args, **kwargs):
        self.emp_id = str(self.user.id)
        super().save(*args, **kwargs)


# show leave


class LeaveDetailList(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'emp_id'
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        emp_id = self.kwargs.get(self.lookup_field)
        if user.id != emp_id:
            return Response({"error": "Unauthorized Access"}, status=status.HTTP_401_UNAUTHORIZED)

        leave_data = self.queryset.filter(emp_id=emp_id)
        serializer = self.serializer_class(leave_data, many=True)
        return Response(serializer.data)


class SortedLeavesView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = LeaveApplicationSerializer

    def get_queryset(self):
        emp_id = self.kwargs.get('emp_id')
        sort = self.kwargs.get('sort')
        if sort == 'asc':
            queryset = LeaveApplication.objects.filter(
                emp_id=emp_id).order_by('first_Day')
        elif sort == 'desc':
            queryset = LeaveApplication.objects.filter(
                emp_id=emp_id).order_by('-first_Day')
        else:
            queryset = LeaveApplication.objects.filter(emp_id=emp_id)

        user = self.request.user
        if user.id != emp_id:
            raise PermissionDenied("Unauthorized Access")

        return queryset


class SearchLeaveView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = LeaveApplicationSerializer

    def get_queryset(self):
        emp_id = self.kwargs.get('emp_id')
        first_Day = self.kwargs.get('first_Day')

        user = self.request.user
        if user.id != emp_id:
            raise PermissionDenied("Unauthorized Access")

        return LeaveApplication.objects.filter(emp_id=emp_id, first_Day=first_Day)


class LogoutUser(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return Response({"error": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Token deleted successfully"}, status=status.HTTP_200_OK)
