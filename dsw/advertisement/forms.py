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


SEARCH_OPTIONS = (
    ('type', ('Tipo')),
    ('availability', ('Disponibilidade')),
)

class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    search_option = forms.ChoiceField(choices=SEARCH_OPTIONS, widget=forms.RadioSelect(attrs={'class': 'radio'}))