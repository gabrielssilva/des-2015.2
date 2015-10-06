from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from forms import UserForm
from forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from coop.models import User

#Initial page
def home(request):
	return render(request, "index.html")

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


#Page for register user
class Register(CreateView):
	template_name = 'register.html'
	fields = ['nome', 'email', 'telefone', 'senha']
	model = User
	success_url = reverse_lazy('list')

class List(ListView):
	template_name = 'list.html'
	model = User
	context_object = 'name'
