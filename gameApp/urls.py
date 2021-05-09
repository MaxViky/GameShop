from urllib import request

from django.conf.urls import url
from django.urls import path

from . import views
from .views import GameView

urlpatterns = [
    url('^$', GameView.GetGamesPage),
    url('^search/', views.SearchView.as_view(), name='search'),
    path('<slug:slug>/', GameView.showDetailView),

]