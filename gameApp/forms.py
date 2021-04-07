from django import forms


class filterForm(forms.Form):
    name = forms.CharField(required=False)