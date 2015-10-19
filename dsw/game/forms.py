from django import forms
from .models import Game, Advertisement
from coop.models import Player

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['nome', 'console', 'genero', 'linguagem', 'estado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'console': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'linguagem': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ['data', 'tipo', 'disponibilidade']
        widgets = {
            'data': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'disponibilidade': forms.TextInput(attrs={'class': 'form-control'}),
        }