from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput

from userApp.models import Profile


class loginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', required=False)
    password = forms.CharField(label='Пароль', required=False, widget=PasswordInput())


class regForms(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', required=False, widget=PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', required=False, widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


