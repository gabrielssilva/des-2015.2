from django import forms
from models import Game, Advertisement
from coop.models import Player

class GameForm(forms.ModelForm):
   

    class Meta:
        model = Game
        fields = ['nome', 'console', 'genero', 'linguagem', 'estado']

class AdvertisementForm(forms.ModelForm):

	class Meta:
		model = Advertisement
		fields = ['data', 'tipo', 'disponibilidade']


