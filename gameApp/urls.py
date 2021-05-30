from urllib import request

from django.conf.urls import url
from django.urls import path

from . import views
from .views import GameView

urlpatterns = [
    url('^$', GameView.GetGamesPage, name='shop_frame'),
    url('^search/', views.SearchView.as_view(), name='search'),
    url('^sort/', GameView.sort, name='sort'),
    path('<slug:slug>/', GameView.showDetailView),

]