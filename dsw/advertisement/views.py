from django.shortcuts import render
from .forms import AdvertisementForm
from .models import Advertisement
from django.views.generic import View
from django.views.generic import CreateView, ListView

# Create your views here.

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


class Advertisement(CreateView):
	template_name = 'advertisement.html'
	fields = ['data', 'tipo', 'disponibilidade']
	model = Advertisement

class List(ListView):
	template_name = 'list_advertisements.html'
	model = Advertisement
	context_object = 'name'