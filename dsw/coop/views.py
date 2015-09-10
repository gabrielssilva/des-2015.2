from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

#Initial page
def index(request):
	return render_to_response("index.html")

#Page for register user
def register(request):

	if request.method=='POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/login")
		else:
			return render(request, "register.html", {"form": form})

	return render(request, "register.html", {"form": UserCreationForm()})