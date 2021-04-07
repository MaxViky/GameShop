from django.core.paginator import *
from django.shortcuts import render
from django.views.generic.base import View

from gameApp.models import*


class GameView(View):
    def get(self, request):
        games = Game.objects.all()
        paginator = Paginator(games, 1)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'templates/gamesPage.html',
                      {'page': page, 'posts': posts})


class DetailGameView(View):
    def get(self, request, slug):
        game = Game.objects.get(url=slug)
        gameShots = GameShots.objects.filter(game=game)
        return render(request, 'templates/gameInfoPage.html', {'game': game, 'gameShots': gameShots})

