from django.http import HttpResponseRedirect
from django.contrib import messages

# Checks for user authentication
def signed_in(func):
    def wrapper(self, request, *args, **kwargs):
        if (request.user.is_authenticated()):
            return func(self, request, *args, **kwargs)
        else:
            messages.warning(request, 'Log in to access this page.')
            return HttpResponseRedirect('/')
    return wrapper