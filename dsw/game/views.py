from django.shortcuts import render
from .forms import GameForm, AdvertisementForm
from coop.models import Player
from .models import Game, Advertisement
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, CreateView, ListView
from django.forms.formsets import formset_factory


# def advertisement(request):
# 	if request.method == 'POST':
# 		form = AdvertisementForm(data=request.POST)

# 		if form.is_valid():
# 			advertisement = form.save()
# 			advertisement.save()

# 			return render(request, 'index.html')
# 		else:
# 			print(form.errors)
# 	else:
# 		form = AdvertisementForm()

# 	return render(request, 'advertisement.html', {'form': form})


class AdvertisementView(View):
	http_method_names = [u'get', u'post']

	def post(self, request):
		GameFormSet = formset_factory(GameForm)
		form = AdvertisementForm(data=request.POST)
		game_formset = GameFormSet(data=request.POST)

		advertisement = form.save()
		for gameform in game_formset:
			
			game = gameform.save(commit=False)
			game.player_id = request.user
			game.save()
			advertisement.games.add(game)

		form = AdvertisementForm()
		return render(request, 'advertisement.html', {'form': form, 'game_formset': GameFormSet})

	def get(self, request):
		form = AdvertisementForm()
		GameFormSet = formset_factory(GameForm)
		return render(request, 'advertisement.html', {'form': form, 'game_formset': GameFormSet})


class GameView(View):
	http_method_names = [u'get', u'post']

	def post(self, request):
		form = GameForm(data=request.POST)
		game = form.save(commit=False)
		game.player_id = request.user
		game.save()
		return render(request, 'advertisement.html', {'form': AdvertisementForm()})

	def get(self, request):
		return render(request, 'create_game.html', {'form': GameForm()})


# class Game(CreateView):
# 	template_name = 'create_game.html'
# 	fields = ['nome', 'console', 'genero', 'linguagem', 'estado']
# 	model  = Game
# 	success_url = reverse_lazy('list_game')

class List(ListView):
	template_name = 'list_game.html'
	model = Game
	context_object = 'name'
