from django.shortcuts import render
from .forms import AdvertisementForm
from .models import Advertisement
from django.views.generic import View

# Create your views here.

class AdvertisementView(View):
	http_method_names = [u'get', u'post']

	def post(self, request):
		form = AdvertisementForm(data=request.POST)

	def get(self, request):
		return render(request, 'advertisement.html', {'form': AdvertisementForm()})