from django.shortcuts import render
from .forms import AdvertisementForm
from game.forms import GameForm
from .models import Advertisement
from django.views.generic import View
from django.views.generic import CreateView, ListView
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
# Create your views here.

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