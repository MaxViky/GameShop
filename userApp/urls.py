from django.conf.urls import url
from . import views

urlpatterns = [
    url('^join/$', views.register),
    url('^login/$', views.LogIn),
    url('^logout/$', views.LogOut),
]