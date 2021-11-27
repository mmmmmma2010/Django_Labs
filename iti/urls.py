from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from iti import views

urlpatterns=[
    path('', views.index, name='index'),

    path('adds', views.addstudent, name='addstudent'),
    path('students', views.get_students, name='students'),
    # path('students', views.StudentList.as_view(), name='students'),
    path('students/<int:sid>', views.get_student, name='studentdetails'),
    path('delstudents/<int:sid>', views.delete_student, name='studentdelete'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='welcome.html'),name='logout'),
    # path('addt', views.addtrack, name='addtrack'),
    # path('tracks', views.get_tracks, name='tracks'),    
    # path('addc', views.addcourse, name='addcourse'),
    # path('students', views.get_courses, name='courses'),
]