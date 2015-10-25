from django.shortcuts import render
from .forms import GameForm
from coop.models import Player
from .models import Game
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, CreateView, ListView
from django.forms.models import modelformset_factory
from advertisement.forms import AdvertisementForm


def create_game(request):
	if request.method == 'POST':
		form = GameForm(data=request.POST)

		if form.is_valid():
			
			#game.player_id = request.user  depois que salva o jogo 
			game = form.save()
			game.save()

			return render(request, 'advertisement.html')
		else:
			print(form.errors)
	else:
		form = GameForm()

	return render(request, 'create_game.html', {'form': form})


class Game(CreateView):
	template_name = 'create_game.html'
	fields = ['nome', 'console', 'genero', 'linguagem', 'estado']
	model  = Game
	success_url = reverse_lazy('list_game')


class List(ListView):
	template_name = 'list_game.html'
	model = Game
	context_object = 'name'
