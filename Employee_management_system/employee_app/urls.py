from django.urls import path
from .views import *


urlpatterns = [

    path('login-user/<str:pk>', EmployeeList.as_view(), name='login'),


]
