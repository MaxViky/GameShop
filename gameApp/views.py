import null as null
from django.core.paginator import *
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View

from gameApp.forms import filterForm
from gameApp.models import*


class GameView(View):
    def get(self, request):
        games = Game.objects.all()
        paginator = Paginator(games, 2)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'templates/gamesPage.html',
                      {'game_list': posts})


class DetailGameView(View):
    def get(self, request, slug):
        game = Game.objects.get(url=slug)
        gameShots = GameShots.objects.filter(game=game)
        return render(request, 'templates/gameInfoPage.html', {'game': game, 'gameShots': gameShots})


class SearchView(View):
    def get(self, request, *args, **kwargs):
        posts = {}

        question = request.GET.get('q')
        if question is not None:
            search_game = Game.objects.filter(Q(name__icontains=question))
            posts['last_question'] = '?q=%s' % question

            paginator = Paginator(search_game, 2)
            page = request.GET.get('page')
            try:
                posts['game_list'] = paginator.page(page)
            except PageNotAnInteger:
                posts['game_list'] = paginator.page(1)
            except EmptyPage:
                posts['game_list'] = paginator.page(paginator.num_pages)

        return render(request, template_name='templates/gamesPage.html', context=posts)

