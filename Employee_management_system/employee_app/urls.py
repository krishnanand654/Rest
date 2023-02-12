from django.urls import path
from .views import *


urlpatterns = [


    path('leavec/<int:user_id>/', LeaveView.as_view(), name='leave'),
    path('myleave/<str:id>/', MyLeaveView.as_view(), name='leave'),
    # path('sort-leaves/', LeaveAppSort.as_view(), name='sort-leaves'),
    path('sorted-leaves/<int:emp_id>/<str:sort>/',
         SortedLeavesView.as_view(), name='sorted_leaves'),
    path('search_leave/<int:emp_id>/<str:first_Day>/',
         SearchLeaveView.as_view(), name='search_leave'),

]
