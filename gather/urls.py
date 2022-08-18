from django.urls import path
from . import views


urlpatterns = [
    path('new', views.new, name='new'),
    #path('nominal', views.nominal, name='nominal'),
    path('newexam', views.newexam, name='newexam'),
    path('paperinfo', views.paperinfo, name='paperinfo'),
    path('studentinfo', views.studentinfo, name='studentinfo'),
    path('hallinfo', views.hallinfo, name='hallinfo'),
    path('invigilatorinfo', views.invigilatorinfo, name='invigilatorinfo'),
    path('addhall', views.addhall, name='addhall'),
    path('addInvigilator', views.addInvigilator, name = 'addInvigilator'),
    path('hedit', views.hedit,name = 'hedit'),
    path('hdelete', views.hdelete, name='hdelete'),
    path('iedit', views.iedit,name= 'iedit'),
    path('idelete', views.idelete, name='idelete'),
    path('examinfo', views.examinfo, name='examinfo'),
    #path('edelete', views.edelete, name='edelete'),
    #path('selectpexam', views.selectpexam, name='selectpexam'),
    #path('selectsexam', views.selectsexam, name='selectsexam'),
    #path('addstudent', views.addstudent, name='addstudent'),
    path('addpaper', views.addpaper, name='addpaper'),
    path('pfileupload', views.pfileupload, name='pfileupload'),
    path('sfileupload', views.sfileupload, name='sfileupload'),
    path('pdelete', views.pdelete, name='pdelete'),
    path('sdelete', views.sdelete, name='sdelete'),
    #path('selecttexam', views.selecttexam, name='selecttexam'),
    #path('addtimetable', views.addtimetable, name='addtimetable'),
    #path ('tdelete', views.tdelete, name='tdelete'),
    path('selectexam', views.selectexam, name='selectexam'),
    path('about', views.about, name='about'),
]