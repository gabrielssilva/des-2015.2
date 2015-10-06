# -*- coding: utf-8 -*-
from django.forms import PasswordInput
from django import forms
from models import User

class UserForm(forms.ModelForm):

        class Meta:
                model = User
                fields = ['nome', 'email', 'telefone']
              	widgets = {
            		'senha': PasswordInput()
        		}

class AuthenticationForm(forms.Form):

    nome = forms.CharField(max_length=254)
    senha = forms.CharField(widget=forms.PasswordInput)
