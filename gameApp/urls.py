from urllib import request

from django.conf.urls import url
from django.urls import path

from . import views
from .views import GameView

urlpatterns = [
    url('^$', views.GameView.GetGamesPage, name='shop_frame'),
    url('^search/', views.SearchView.as_view(), name='search'),
    url('^filter/', views.FilterView.as_view(), name='filter'),
    url('^sort/', views.SortView.as_view(), name='sort'),
    path('<slug:slug>/', GameView.showDetailView),
]