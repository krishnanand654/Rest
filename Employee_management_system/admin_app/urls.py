from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [



    # path('login/', LoginView.as_view(), name='login'),
    path('create/', EmployeeCreate.as_view(), name='create'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>',
         EmployeeDetail.as_view(), name='employee-detail'),
    path('employees/delete/<int:pk>/',
         EmployeeDeleteDetail.as_view(), name='employee-delete-detail'),
    path('employees/update/<int:pk>/',
         EmployeeUpdateDetail.as_view(), name='employee-update-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')

    path('leavecreate', LeaveCreate.as_view(), name='create'),
    path('leaves',
         LeaveList.as_view(), name='employee-detail'),
    path('leave/<int:pk>', LeaveView.as_view(), name='leave'),



]
