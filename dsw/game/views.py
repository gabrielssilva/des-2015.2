from django.shortcuts import render
from forms import GameForm
from coop.models import Player
from game.models import Game
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView


def create_game(request):
	if request.method == 'POST':
		form = GameForm(data=request.POST)

		if form.is_valid():
			game = form.save()
			game.save()

			return render(request, 'index.html')
		else:
			print form.errors
	else:
		form = GameForm()

	return render(request, 'advertisement.html', {'form': form})

class Game(CreateView):
	template_name = 'advertisement.html'
	fields = ['nome', 'console', 'genero', 'linguagem', 'estado']
	model  = Game
	success_url = reverse_lazy('list_game')

class List(ListView):
	template_name = 'list_game.html'
	model = Game
	context_object = 'name'

