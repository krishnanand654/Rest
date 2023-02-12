from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render
from admin_app.models import EmployeeModel, LeaveApplication
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, MultiPartParser

from .serializers import LeaveApplicationSerializer


# Create your views here.

from rest_framework import generics
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


class LeaveView(APIView):
    parser_classes = [MultiPartParser]
    serializer_class = LeaveApplicationSerializer

    def post(self, request, user_id):

        employee = EmployeeModel.objects.get(Employee_Id=user_id)

        emp_id = employee.Employee_Id
        emp_name = employee.Employee_Name
        leave = LeaveApplication.objects.create(

            user=employee,
            emp_id=emp_id,
            emp_name=emp_name,

            apply_date=request.data.get('apply_date'),
            nature_of_leave=request.data.get('nature_of_leave'),
            first_Day=request.data.get('first_Day'),
            last_Day=request.data.get('last_Day'),
            # number_Of_Days=request.data.get('number_Of_Days'),
            # pending,approved,rejected,cancelled

        )
        return Response({'status': 'Leave request created'})


class MyLeaveView(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    serializer_class = LeaveApplicationSerializer

    def get_object(self):
        id = self.kwargs['id']
        return get_object_or_404(LeaveApplication.objects.all(), emp_id=id)


class LeaveDetailList(generics.ListAPIView):
    # authentication_classes = (EmployeeAuthentication,)
    lookup_field = 'emp_id'  # details of particular employee
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get(self.lookup_field)
        leave_data = self.queryset.filter(emp_id=id)
        serializer = LeaveApplicationSerializer(leave_data, many=True)
        return Response(serializer.data)


# class LeaveAppSort(generics.ListAPIView):
#     serializer_class = LeaveApplicationSerializer

#     def get_queryset(self):
#         sort = self.request.query_params.get('sort', 'asc')
#         if sort == 'asc':
#             return LeaveApplication.objects.all().order_by('apply_date')
#         else:
#             return LeaveApplication.objects.all().order_by('-apply_date')


class SortedLeavesView(generics.ListAPIView):
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
        return queryset


class SearchLeaveView(generics.ListAPIView):
    serializer_class = LeaveApplicationSerializer

    def get_queryset(self):
        emp_id = self.kwargs['emp_id']
        first_Day = self.kwargs['first_Day']
        return LeaveApplication.objects.filter(emp_id=emp_id, first_Day=first_Day)
