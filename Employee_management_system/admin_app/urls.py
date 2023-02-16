from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', EmployeeCreate.as_view(), name='create'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employee/<int:pk>',
         EmployeeDetail.as_view(), name='employee-detail'),
    path('employee/delete/<int:pk>/',
         EmployeeDeleteDetail.as_view(), name='employee-delete-detail'),
    path('employee/update/<int:pk>/',
         EmployeeUpdateDetail.as_view(), name='employee-update-detail'),
    path('leaves/', LeaveList.as_view(), name='leaves'),
    path('leaveapprove/<str:user_id>/',
         LeaveApprove.as_view(), name='leaveapprove'),
    path('leaveapprove/<str:user_id>/<int:leaveid>/', LeaveApprove.as_view(),
         name='leaveapprove2'),
    path('leave/<str:status>/', ApprovedLeavesList.as_view(), name='leavestatus'),
    path('sortemployees/<str:sort>/',
         SortedEmployeeView.as_view(), name='sort-leaves'),
    path('searchemployee/<int:emp_id>/',
         SearchEmployeeView.as_view(), name='search_leaves'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
