from django.shortcuts import render
from .forms import GameForm, AdvertisementForm
from coop.models import Player
from game.models import Game, Advertisement
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView


def create_game(request):
	if request.method == 'POST':
		form = GameForm(data=request.POST)

		if form.is_valid():
			#game = form.save(commit=False) conserta o erro, mas some com o botão de logout e com o form anúncio
			#game.player_id = request.user  depois que salva o jogo 
			game = form.save()
			game.save()

			return render(request, 'advertisement.html')
		else:
			print(form.errors)
	else:
		form = GameForm()

	return render(request, 'create_game.html', {'form': form})

def advertisement(request):
	if request.method == 'POST':
		form = AdvertisementForm(data=request.POST)

		if form.is_valid():
			advertisement = form.save()
			advertisement.save()

			return render(request, 'index.html')
		else:
			print(form.errors)
	else:
		form = AdvertisementForm()

	return render(request, 'advertisement.html', {'form': form})


class Game(CreateView):
	template_name = 'create_game.html'
	fields = ['nome', 'console', 'genero', 'linguagem', 'estado']
	model  = Game
	success_url = reverse_lazy('list_game')

class List(ListView):
	template_name = 'list_game.html'
	model = Game
	context_object = 'name'


class Advertisement(CreateView):
	template_name = 'advertisement.html'
	fields = ['data', 'tipo', 'disponibilidade']
	model = Advertisement
