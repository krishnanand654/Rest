
from rest_framework import generics

from rest_framework.response import Response

from rest_framework import generics, permissions
from django.shortcuts import render
from rest_framework.parsers import JSONParser, MultiPartParser
from .models import EmployeeModel, LeaveApplication
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeCreateSerializer, EmployeeListSerializer, EmployeeDetailSerializer, LeaveListSerializer, LeaveApproveSerializer, UserSerializer

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404




from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        
        try:
            token = authorization_header.split(' ')[1]
        except (IndexError, AttributeError):
            raise AuthenticationFailed('Invalid Authorization header format')
        
        validated_token = self.get_validated_token(token)
        user = self.get_user(validated_token)
        return (user, validated_token)

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class EmployeeCreate(generics.CreateAPIView):  # create employee
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeCreateSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    # parser_classes = (MultiPartParser, JSONParser)


class EmployeeList(generics.ListAPIView):  # list  all employee
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeListSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]


class EmployeeDetail(generics.RetrieveAPIView):
    lookup_field = 'pk'  # details of particular employee
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]


class EmployeeUpdateDetail(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'  # details of particular employee
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]


class EmployeeDeleteDetail(generics.RetrieveDestroyAPIView):
    lookup_field = 'pk'
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeCreateSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]


class LeaveList(generics.ListAPIView):  # list  all employee
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveListSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]


class LeaveApprove(generics.RetrieveUpdateAPIView):  # list  all employee

    parser_classes = (MultiPartParser, JSONParser)
    lookup_field = 'user_id'
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApproveSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get_object(self):
        id = self.kwargs.get(self.lookup_field)
        l_id = self.kwargs.get('leaveid')
        if l_id is not None:
            return get_object_or_404(self.queryset, user=id, id=l_id)
        else:
            return get_object_or_404(self.queryset, user=id)

    def save(self, *args, **kwargs):
        self.emp_id = str(self.user.Employee_Id)
        super().save(*args, **kwargs)
        


class ApprovedLeavesList(generics.ListAPIView):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveListSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get_queryset(self):
        status = self.kwargs.get('status')
        if status == 'approved':
            return self.queryset.filter(status='approved')
        elif status == 'pending':
            return self.queryset.filter(status='pending')


class SortedEmployeeView(generics.ListAPIView):
    serializer_class = EmployeeListSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]    

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
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get_queryset(self):
        emp_id = self.kwargs['emp_id']
        return EmployeeModel.objects.filter(Employee_Id=emp_id)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = ""
        user.save()
        return Response({"message": "Successfully logged out."}, status=200)
