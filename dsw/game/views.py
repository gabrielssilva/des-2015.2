from django.shortcuts import render
from .forms import GameForm
from coop.models import Player
from .models import Game
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, CreateView, ListView
from django.http import HttpResponse
from advertisement.forms import AdvertisementForm
from .forms import GameForm
from django.forms.formsets import formset_factory


def new_game_form(request):
	GameFormSet = formset_factory(GameForm)
	form = AdvertisementForm(data=request.POST)
	form_data = request.POST.copy()
	print(form_data)
	form_data['form-TOTAL_FORMS'] = int(form_data["form-TOTAL_FORMS"])+1
	game_formset = GameFormSet(data=form_data)

	return render(request, 'advertisement.html', {'form': form, 'game_formset': game_formset})


class Game(CreateView):
	template_name = 'create_game.html'
	fields = ['nome', 'console', 'genero', 'linguagem', 'estado']
	model  = Game
	success_url = reverse_lazy('list_game')


class List(ListView):
	template_name = 'list_game.html'
	model = Game
	context_object = 'name'