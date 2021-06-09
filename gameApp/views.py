import null as null
from django.core.paginator import *
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from gameApp.models import*


class GameView(View):
    def GetGamesPage(request) -> render:
        games = Game.objects.all()
        paginator = Paginator(games, 10)
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
        if request.user.is_authenticated:
            lib = GameLibrary.objects.filter(user=request.user, game=game)
            cart = Cart.objects.filter(user=request.user, game=game)
            if request.POST:
                if 'add' in request.POST:
                    var = Cart()
                    var.game = game
                    var.user = request.user
                    var.save()
            cart = len(cart)
            lib = len(lib)
        else:
            lib = null
            cart = null
            if request.POST:
                if 'add' in request.POST:
                    return redirect("/login")
        return render(request, 'templates/gameInfoPage.html',
                            {'game': game, 'gameShots': gameShots, 'tags': tags, 'cart': cart, 'lib': lib})

    def sort(request):
        games = Game.objects.all()

        return render(request, 'templates/gamesPage.html',
                      {'game_list': games})


class SearchView(View):
    def get(self, request, *args, **kwargs):
        games = {}
        question = request.GET.get('name')
        if question is not None:
            search_game = Game.objects.filter(Q(name__icontains=question))
            games['last_question'] = '?name=%s' % question
            paginator = Paginator(search_game, 10)
            page = request.GET.get('page')
            try:
                games['game_list'] = paginator.page(page)
            except PageNotAnInteger:
                games['game_list'] = paginator.page(1)
            except EmptyPage:
                games['game_list'] = paginator.page(paginator.num_pages)
        return render(request, template_name='templates/gamesPage.html', context=games)


class FilterView(View):
    def get(self, request, *args, **kwargs):
        games = {}
        range = request.GET.get('range')
        if range is not None:
            range = str(range).split(';')
            minPrice = int(range[0])
            maxPrice = int(range[1])
            filter_game = Game.objects.filter(Q(price__range=(minPrice, maxPrice)))
            games['last_question'] = '?range=%s' % range
            paginator = Paginator(filter_game, 10)
            page = request.GET.get('page')
            try:
                games['game_list'] = paginator.page(page)
            except PageNotAnInteger:
                games['game_list'] = paginator.page(1)
            except EmptyPage:
                games['game_list'] = paginator.page(paginator.num_pages)
        return render(request, template_name='templates/gamesPage.html', context=games)


class SortView(View):
    def get(self, request, *args, **kwargs):
        games = {}
        sort_value = request.GET.get('radio_button')
        if sort_value is not None:
            if sort_value == '1':
                sort_game = Game.objects.order_by("name")
            elif sort_value == '2':
                sort_game = Game.objects.order_by("-name")
            elif sort_value == '3':
                sort_game = Game.objects.order_by("price")
            elif sort_value == '4':
                sort_game = Game.objects.order_by("-price")
            elif sort_value == '5':
                sort_game = Game.objects.order_by("release")
            elif sort_value == '6':
                sort_game = Game.objects.order_by("-release")
            games['last_sort_value'] = '?sort_value=%s' % sort_value
            paginator = Paginator(sort_game, 10)
            page = request.GET.get('page')
            try:
                games['game_list'] = paginator.page(page)
            except PageNotAnInteger:
                games['game_list'] = paginator.page(1)
            except EmptyPage:
                games['game_list'] = paginator.page(paginator.num_pages)
            return render(request, template_name='templates/gamesPage.html', context=games)


class Library(View):
    def get(request):
        lib = GameLibrary.objects.filter(user=request.user)
        paginator = Paginator(lib, 5)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return posts


class CartUser(View):
    def get(request):
        cart = Cart.objects.filter(user=request.user)
        return cart
