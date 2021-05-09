from django import forms

from gameApp import models
from gameApp.models import Publisher, Developer




class filterForm(forms.Form):
    price = forms.CharField(label='Цена', required=False)
    publisher = forms.MultipleChoiceField(label='Издатель', required=False)
    developer = forms.MultipleChoiceField(label='Разработчик', required=False)
    rating = forms.CharField(label='Рейтинг', required=False)
    release = forms.MultipleChoiceField(label='Дата релиза', required=False)


