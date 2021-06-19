from django.conf.urls import url
from django.urls import path

from . import views
from .views import ProfileView

urlpatterns = [
    url('^join/$', views.register),
    url('^login/$', views.LogIn),
    url('^logout/', views.LogOut, name='logout'),
    path('profile/<str:user>/', ProfileView.getProfile),
    path('profile/edit/<str:user>/', ProfileView.editProfile, name='edit_profile'),
    path('profile/<str:user>/cart/', ProfileView.getCart, name='user_cart'),
    path('profile/<str:user>/history-pay/', ProfileView.getHistoryPay, name='history_pay'),
]