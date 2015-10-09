from django import forms
from models import Game, Advertisement

class GameForm(forms.ModelForm):
    
    class Meta:
        model = Game
        fields = ['nome', 'console', 'genero', 'linguagem', 'estado']

class AdvertisementForm(forms.ModelForm):

	class Meta:
		model = Advertisement
		fields = ['disponibilidade']


