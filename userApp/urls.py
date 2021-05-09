from django.conf.urls import url
from django.urls import path

from . import views
from .views import ProfileView

urlpatterns = [
    url('^join/$', views.register),
    url('^login/$', views.LogIn),
    url('^logout/', views.LogOut, name='logout'),
    path('profile/<str:user>/', ProfileView.getProfile),

]