from django.urls import path
from . import views

urlpatterns = [
    path('allocate', views.allocate, name='allocate'),
    path('vpapers', views.vpapers, name='vpapers'),
    #path('vstudents', views.vstudents, name = 'vstudents'),
    path('vinvigilators', views.vinvigilators, name='vinvigilators'),
    path('vhalls', views.vhalls, name='vhalls'),
    #path('tgenerate', views.tgenerate, name='tgenerate'),
    #path('managetemp', views.managetemp ,name='managetemp'),
    path('edelete', views.edelete, name = 'edelete'),
    path('viewseating', views.viewseating, name = 'viewseating'),
    path('aaselect', views.aaselect, name='aaselect'),
]