from django.contrib import admin
from admin_app.models import EmployeeModel
from admin_app.models import LeaveApplication
# Register your models here.
admin.site.register(EmployeeModel)
admin.site.register(LeaveApplication)
