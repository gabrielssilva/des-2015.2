from django import forms
from .models import Game
from coop.models import Player

CONSOLE = (
    ('01', ('PC')),
    ('02', ('Xbox')),
    ('03', ('Xbox 360')),
    ('04', ('Xbox One')),
    ('05', ('Playstation')),
    ('06', ('Playstation 2')),
    ('07', ('Playstation 3')),
    ('08', ('Playstation 4')),
)

GENRE = (
    ('01', ('Ação')),
    ('02', ('Aventura')),
    ('03', ('FPS')),
    ('04', ('RPG')),
    ('05', ('Corrida')),
    ('06', ('Esporte')),
    ('07', ('Terror')),
    ('08', ('Luta')),
)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['nome', 'console', 'genero', 'linguagem', 'estado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'console': forms.Select(attrs={'class': 'dropdown form-control'}, choices=CONSOLE),
            'genero': forms.Select(attrs={'class': 'dropdown form-control'}, choices=GENRE),
            'linguagem': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }