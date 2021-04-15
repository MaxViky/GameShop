from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('^join/$', views.register),
    url('^login/$', views.LogIn),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]