from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from coop.factory import PlayerFactory


class Player(AbstractBaseUser):
	nome = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	senha = models.CharField(max_length=50)
	telefone = PhoneNumberField()
	is_staff=True

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nome', 'telefone']
	objects = PlayerFactory()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = (u'name')
		verbose_name_plural = (u'names')