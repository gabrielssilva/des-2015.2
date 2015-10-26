from django import forms
from .models import Advertisement
from coop.models import Player
from game.models import Game

class AdvertisementForm(forms.ModelForm):
    jogos = forms.ModelMultipleChoiceField(queryset=Game.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Advertisement
        fields = ['data', 'tipo', 'disponibilidade']
        widgets = {
            'data': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'disponibilidade': forms.TextInput(attrs={'class': 'form-control'}),
        }