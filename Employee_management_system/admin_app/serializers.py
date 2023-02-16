from rest_framework import serializers
from admin_app.models import EmployeeModel, LeaveApplication
from django.contrib.auth.models import User


class EmployeeCreateSerializer(serializers.ModelSerializer):
    Profile_Picture = serializers.ImageField(
        max_length=None, use_url=True, required=False,)

    class Meta:
        model = EmployeeModel
        fields = ('Employee_Name', 'Contact_Number', 'Emergency_Contact_Number', 'Address', 'Postion', 'DOB', 'Martial_status', 'Blood_Group', 'Job_Title',
                  'work_Location', 'Reporting_to', 'Linked_In', 'Profile_Picture', 'Email', 'Password',)

    # def save(self):
    #     emp = User(
    #         email=self.validated_data['Email'], username=self.validated_data['Email'],)
    #     Password = self.validated_data['Password']
    #     emp.set_password(Password)
    #     emp.save()
    #     return emp


class EmployeeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeModel
        fields = ('Employee_Id', 'Employee_Name', 'Contact_Number',
                  'Email', 'Postion', 'Reporting_to', 'work_Location',)


class EmployeeDetailSerializer(serializers.ModelSerializer):
    lookup_field = 'pk'

    class Meta:
        model = EmployeeModel
        fields = '__all__'

class LeaveListSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeModel
        fields = ('__all__')

class LeaveDetailSerializer(serializers.Serializer):
    Email = serializers.EmailField()


class LeaveCreateSerializer(serializers.ModelSerializer):
    lookup_field = 'pk'

    class Meta:
        model = LeaveApplication
        fields = ('user', 'first_Day')
