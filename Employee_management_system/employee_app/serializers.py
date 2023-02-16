from rest_framework import serializers
from admin_app.models import LeaveApplication, EmployeeModel

from django.contrib.auth.models import User

from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    
    lookup_field = 'pk'
    class Meta:
        model = EmployeeModel
        fields = ('user',)
        
