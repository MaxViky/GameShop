import null as null
from django.core.paginator import *
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from gameApp.forms import filterForm
from gameApp.models import*


class GameView(View):
    def GetGamesPage(request) -> render:
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

    def showDetailView(request, slug) -> render:
        game = Game.objects.get(url=slug)
        gameShots = GameShots.objects.filter(game=game)
        tags = Tagged.objects.filter(game=game)
        cart = Cart.objects.filter(user=request.user, game=game)
        if request.POST:
            if 'add' in request.POST:
                var = Cart()
                var.game = game
                var.user = request.user
                var.save()

        return render(request, 'templates/gameInfoPage.html', {'game': game, 'gameShots': gameShots, 'tags': tags, 'cart': len(cart)})




class SearchView(View):
    def get(self, request, *args, **kwargs):
        games = {}
        question = request.GET.get('name')

        if question is not None:
            search_game = Game.objects.filter(Q(name__icontains=question))
            games['last_question'] = '?name=%s' % question
            paginator = Paginator(search_game, 2)
            page = request.GET.get('page')
            try:
                games['game_list'] = paginator.page(page)
            except PageNotAnInteger:
                games['game_list'] = paginator.page(1)
            except EmptyPage:
                games['game_list'] = paginator.page(paginator.num_pages)

        return render(request, template_name='templates/gamesPage.html', context=games)

