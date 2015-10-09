from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from forms import PlayerForm
from forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render
from coop.models import Player


class Auth(object):
    @staticmethod
    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user and user.is_active:
                auth_login(request, user)
                return render(request, "index.html")

        return render(request, "login.html", {"form": AuthenticationForm()})

    @staticmethod
    def logout(request):
        auth_logout(request)
        return render(request, "index.html")

    @staticmethod
    def register(request):
        if request.method == 'POST':
            form = PlayerForm(data=request.POST)

            if form.is_valid():
                Player.objects.create_user(form)
                return render(request, 'index.html')
            else:
                print form.errors
        else:
            form = PlayerForm()

        return render(request, 'register.html', {'form': form})



class Home(TemplateView):
    template_name = 'index.html'



#Page for register user
class Register(CreateView):
	template_name = 'register.html'
	fields = ['nome', 'email', 'telefone', 'senha']
	model = Player
	success_url = reverse_lazy('list')

#Page for list users
class List(ListView):
	template_name = 'list.html'
	model = Player
	context_object = 'name'
