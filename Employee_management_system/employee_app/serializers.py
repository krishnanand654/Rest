from rest_framework import serializers
from admin_app.models import LeaveApplication, EmployeeModel


from django.contrib.auth.models import User

from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ('Email', 'Password')
        extra_kwargs = {'Password': {'write_only': True}}


class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = ('apply_date', 'nature_of_leave',
                  'first_Day', 'last_Day')


# class LeavePreviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LeaveApplication
#         fields = ('emp_id', 'emp_name', 'apply_date', 'nature_of_leave',
#                   'first_Day', 'last_Day')
