# -*- coding: utf-8 -*-
from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Player
        fields = ['email', 'password', 'nome', 'telefone']

class AuthenticationForm(forms.Form):
    email = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
