from django.shortcuts import render
from .forms import AdvertisementForm, SearchForm
from game.forms import GameForm
from .models import Advertisement
from django.views.generic import View
from django.views.generic import CreateView, ListView
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from abc import ABCMeta, abstractmethod


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
		return HttpResponseRedirect('/advertisement/list_advertisiments')

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
			search_strategy = TypeSearchStrategy(request.POST['search_text'])
		elif (request.POST['search_option'][0] == 'availability'):
			search_strategy = AvailabilitySearchStrategy(request.POST['search_text'])

		self.object_list = self.filter(search_strategy)
		return render(request, 'list_advertisements.html', {'search_form': SearchForm(), 'object_list': self.object_list})

	def filter(self, search_strategy):
		return search_strategy.filter_content()


class SearchStrategy:
	__metaclass__ = ABCMeta

	def __init__(self, search_text):
		self.search_text = search_text

	@abstractmethod
	def filter_content(self, search_text):
		pass


class TypeSearchStrategy(SearchStrategy):
	def filter_content(self):
		return Advertisement.objects.filter(tipo__icontains=self.search_text)


class AvailabilitySearchStrategy(SearchStrategy):
	def filter_content(self):
		return Advertisement.objects.filter(disponibilidade__icontains=self.search_text)
