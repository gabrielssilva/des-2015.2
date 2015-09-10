from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from coop.models import User

#Initial page
def home(request):
	return render(request, "index.html")

#Page for register user
class Register(CreateView):
	template_name = 'register.html'
	model = User
	success_url = reverse_lazy('list')

class List(ListView):
	template_name = 'list.html'
	model = User
	context_object = 'name'