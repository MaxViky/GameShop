import datetime
from django import forms

from gameApp import models
from gameApp.models import Publisher, Developer


def fill_release():
    now = datetime.datetime.now()
    release = []
    i = 1970
    for i in range(now.year-i):
        release.append(i)
    return release


class filterForm(forms.Form):
    price = forms.CharField(label='Цена', required=False)
    publisher = forms.CharField(label='Издатель', required=False)
    developer = forms.CharField(label='Разработчик', required=False)
    rating = forms.CharField(label='Рейтинг', required=False)
    release = forms.CharField(label='Год выпуска', required=False)





