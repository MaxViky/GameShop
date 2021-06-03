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
        gameform = filterForm(request.GET)
        if 'filter' in request.GET:
            if gameform.is_valid():
                if gameform.cleaned_data["price"]:
                    games = games.filter(price__lte=gameform.cleaned_data["price"])
                if gameform.cleaned_data["publisher"]:
                    games = games.filter(publisher__name__icontains=gameform.cleaned_data["publisher"])
                if gameform.cleaned_data["developer"]:
                    games = games.filter(developer__name__icontains=gameform.cleaned_data["developer"])
                if gameform.cleaned_data["rating"]:
                    games = games.filter(rating__gte=gameform.cleaned_data["rating"])
                if gameform.cleaned_data["release"]:
                    filter_date=gameform.cleaned_data["release"]
                    games = games.filter(release__gte='{0}-01-01'.format(filter_date)).order_by('release')
            return render(request, 'templates/gamesPage.html',
                          {'game_list': games, 'filter_form': gameform})

        paginator = Paginator(games, 10)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'templates/gamesPage.html',
                      {'game_list': posts, 'filter_form': gameform})

    def showDetailView(request, slug) -> render:
        game = Game.objects.get(url=slug)
        gameform = filterForm(request.GET)
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
                            {'game': game, 'gameShots': gameShots, 'tags': tags, 'cart': cart, 'lib': lib, 'filter_form': gameform})

    def sort(request):
        games = Game.objects.all()
        gameform = filterForm(request.GET)
        if 'price_up' in request.GET:
            games = games.order_by("price")
        if 'price_down' in request.GET:
            games = games.order_by("-price")
        if 'developer_up' in request.GET:
            games = games.order_by("developer__name")
        if 'developer_down' in request.GET:
            games = games.order_by("-developer__name")
        if 'publisher_up' in request.GET:
            games = games.order_by("publisher__name")
        if 'publisher_down' in request.GET:
            games = games.order_by("-publisher__name")
        if 'release_up' in request.GET:
            games = games.order_by("release")
        if 'release_down' in request.GET:
            games = games.order_by("-release")
        return render(request, 'templates/gamesPage.html',
                      {'game_list': games, 'filter_form': gameform})


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
