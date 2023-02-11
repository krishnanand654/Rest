from django.urls import path
from .views import *


urlpatterns = [

    path('login-user/', EmployeeLoginAPIView.as_view(), name='login'),


]
