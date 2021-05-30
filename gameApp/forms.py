import datetime
from django import forms

from gameApp import models
from gameApp.models import Publisher, Developer


def fill_release():
    pass


class filterForm(forms.Form):
    price = forms.CharField(label='Цена', required=False)
    publisher = forms.CharField(label='Издатель', required=False)
    developer = forms.CharField(label='Разработчик', required=False)
    rating = forms.CharField(label='Рейтинг', required=False)
    release = forms.ChoiceField(label='Дата релиза', required=False)





