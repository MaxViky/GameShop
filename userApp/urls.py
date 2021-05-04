from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('^join/$', views.register),
    url('^login/$', views.LogIn),
    url('^logout/', views.LogOut, name='logout'),
    #url('^profile/<slug:slug>', views.profile),

]