from django.shortcuts import render
from django.views.generic.base import View

from gameApp.models import*


class GameView(View):
    def get(self, request):
        games = Game.objects.all()
        return render(request, 'templates/gamesPage.html', {'game_list': games})


class DetailGameView(View):
    def get(self, request, slug):
        game = Game.objects.get(url=slug)
        return render(request, 'templates/gameInfoPage.html', {'game': game})