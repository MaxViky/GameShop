from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url('^$', views.GameView.as_view()),
    path('<slug:slug>/', views.DetailGameView.as_view()),
]