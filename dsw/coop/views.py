from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from forms import PlayerForm
from forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from coop.models import Player


def homeLogged(request):
    return render(request, "logged_index.html")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            #agora, basta logar o usuario
            login(request, form.get_model())
            return HttpResponseRedirect("logged_index.html") # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, "login.html", {"form": form})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    
    return render(request, "login.html", {"form": AuthenticationForm()})



def register(request):
    registered = False

    if request.method == 'POST':
        form = PlayerForm(data=request.POST)

        if form.is_valid():
            player = form.save()
            player.set_password(player.password)
            player.save()
            
            registered = True

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

class List(ListView):
	template_name = 'list.html'
	model = Player
	context_object = 'name'
