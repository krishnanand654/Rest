from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('login/',ObtainAuthTokenView.as_view(), name='login'),
    path('leaveapply/<int:emp_id>/', LeaveView.as_view(), name='leaveapply'),
    path('myleave/<int:emp_id>/', LeaveDetailList.as_view(), name='myleave'),
    path('sortedleaves/<int:emp_id>/<str:sort>/',
         SortedLeavesView.as_view(), name='sorted_leave'),
    path('searchleave/<int:emp_id>/<str:first_Day>/',
         SearchLeaveView.as_view(), name='search_leave'),
    path('logoutuser/', LogoutUser.as_view(), name='logout'),



]
