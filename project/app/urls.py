from django.urls import path 
from .views import *
# from .import HodViews, StaffViews, StudentViews

urlpatterns = [


   # URLS for Staff
    path('staff_home/', staff_home, name="staff_home"),
    path('staff_profile/', staff_profile, name="staff_profile"),


   # URSL for Student
    path('student_home/', student_home, name="student_home"),

]
