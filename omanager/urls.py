from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('selectoexam', views.selectoexam, name='selectoexam'),
    path('selectshedule', views.selectshedule, name='selectshedule'),
    path('selecthall', views.selecthall, name='selecthall'),
    path('oviewseating', views.oviewseating, name='oviewseating'),
    path('attendancemanagement', views.attendancemanagement, name='attendancemanagement'),
    path('invioutput', views.invioutput, name = 'invioutput'),
    path('iselectshedule', views.iselectshedule, name='iselectshedule'),
    path('iselecthall', views.iselecthall, name='iselecthall'),
    path('halloutput', views.halloutput, name='halloutput'),
    path('mselectshedule', views.mselectshedule, name='mselectshedule'),
    path('mselecthall', views.mselecthall, name='mselecthall'),
    path('markattendance', views.markattendance, name='markattendance'),
    path('saveattendance', views.saveattendance, name='saveattendance'),
    path('pselectshedule', views.pselectshedule, name='pselectshedule'),
    path('pselecthall', views.pselecthall, name='pselecthall'),
    path('aselectpaper', views.aselectpaper, name='aselectpaper'),
    path('opattendance', views.opattendance, name='opattendance'),
    path('viewshedule', views.viewshedule, name='viewshedule'),
    path('invigilatorarea', views.viewinvigilatorshedule, name='viewinvigilatorshedule'),
    path('studentarea',views.viewstudentshedule, name='viewstudentshedule'),
    path('handler404' , views.error_404, name='handler404'),
    path('navselectexam', views.navselectexam, name='navselectexam'),
    path('navselectexam2', views.navselectexam2, name='navselectexam2'),
    path('navselectexam23', views.navselectexam23, name='navselectexam23'),
    path('navselectexam24', views.navselectexam24, name='navselectexam24'),
    
]