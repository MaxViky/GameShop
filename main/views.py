import datetime

from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core import mail
from django.shortcuts import render

# Create your views here.
from django.views import View

from gameApp.models import Game


class PopularGames(View):
    def get(self, request):
        year = datetime.datetime.now().year
        games_popular = Game.objects.order_by('count_download')[:5]
        release = '{0}-01-01'.format(year)
        games_new_release = Game.objects.filter(release__gte=release)[:2]
        return render(request, 'templates/main.html',
                      {'games_popular': games_popular,
                       'games_new_release': games_new_release, 'year': year})


class AboutUs(View):
    def get(self, request):
        return render(request, 'templates/aboutUs.html')