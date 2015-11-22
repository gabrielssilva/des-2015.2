from django.shortcuts import render
from .forms import AdvertisementForm, SearchForm
from game.forms import GameForm
from .models import Advertisement
from django.views.generic import View
from django.views.generic import CreateView, ListView
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from abc import ABCMeta, abstractmethod
from dsw.decorator import signed_in



class AdvertisementView(View):
	http_method_names = [u'get', u'post']

	@signed_in
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
		return HttpResponseRedirect('/advertisement/list_advertisiments')

	@signed_in
	def get(self, request):
		form = AdvertisementForm()
		GameFormSet = formset_factory(GameForm, extra=0)
		return render(request, 'advertisement.html', {'form': form, 'game_formset': GameFormSet})


class List(ListView):
	template_name = 'list_advertisements.html'
	model = Advertisement
	context_object = 'name'

	def get(self, request):
		self.object_list = self.get_queryset()
		return render(request, 'list_advertisements.html', {'search_form': SearchForm(), 'object_list': self.object_list})

	def post(self, request):
		if (request.POST['search_option'] == 'type'):
			search_strategy = SearchStrategy(Advertisement.objects, filter_by_type)
		elif (request.POST['search_option'] == 'availability'):
			search_strategy = SearchStrategy(Advertisement.objects, filter_by_availability)
		elif (request.POST['search_option'] == 'game'):
			search_strategy = SearchStrategy(Advertisement.objects, filter_by_game)

		self.object_list = search_strategy.filter_content(request.POST['search_text'])
		return render(request, 'list_advertisements.html', {'search_form': SearchForm(), 'object_list': self.object_list})


class SearchStrategy:
	def __init__(self, manager, filter_content):
		self.manager = manager
		SearchStrategy.filter_content = filter_content

	def filter_content(self, search_text):
		return self.manager.all()


def filter_by_type(self, search_text):
	return self.manager.filter(tipo__icontains=search_text)

def filter_by_availability(self, search_text):
	return self.manager.filter(disponibilidade__icontains=search_text)

def filter_by_game(self, search_text):
	return self.manager.filter(games__nome__icontains=search_text)