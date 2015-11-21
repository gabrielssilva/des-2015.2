# -*- coding: utf-8 -*-
from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Player
        fields = ['email', 'nome', 'telefone', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AuthenticationForm(forms.Form):
    email = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
