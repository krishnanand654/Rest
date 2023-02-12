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

    # def perform_create(self, validated_data):
    #     employee = EmployeeModel.objects.create(**validated_data)
    #     username = validated_data['Email']
    #     password = validated_data['Password']
    #     user = User.objects.create_user(
    #         username=username, password=password)
    #     employee.user = user
    #     employee.save()
    #     return employee

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
    lookup_field = 'pk'

    class Meta:
        model = LeaveApplication

        fields = ('id', 'user', 'emp_name', 'first_Day', 'last_Day',
                  'apply_date', 'nature_of_leave', 'status')


class LeaveApproveSerializer(serializers.ModelSerializer):
    lookup_field = 'pk'

    class Meta:
        model = LeaveApplication

        fields = ('first_Day', 'last_Day',
                  'apply_date', 'nature_of_leave', 'status')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
