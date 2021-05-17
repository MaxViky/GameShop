from django.shortcuts import render

# Create your views here.
from django.views import View

from gameApp.models import Game


class PopularGames(View):
    def get(self, request):
        games_popular = Game.objects.order_by('count_download')[:2]
        games_new_release = Game.objects.order_by('release')[:2]
        return render(request, 'templates/main.html',
                      {'games_popular': games_popular,
                       'games_new_release': games_new_release})

def MainPage(request):
    return render(request, 'templates/main.html')