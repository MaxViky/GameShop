from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('^$', views.PopularGames.as_view()),
    url('aboutUs', views.AboutUs.as_view(), name='about_us')
]