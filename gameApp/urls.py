from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url('^$', views.GameView.as_view()),
    url('^search/', views.SearchView.as_view(), name='search'),
    path('<slug:slug>/', views.DetailGameView.as_view()),
]