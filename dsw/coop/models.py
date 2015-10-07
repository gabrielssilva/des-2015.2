from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class Manager(BaseUserManager):
	def create_user(self, email, nome, telefone, senha):
		# ...
		pass

	def create_superuser(self, email, nome, telefone, senha):
		# We do not have super users...
		pass

class Player(AbstractBaseUser):
	nome = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	senha = models.CharField(max_length=50)
	telefone = PhoneNumberField()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nome', 'telefone']
	objects = Manager()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = (u'name')
		verbose_name_plural = (u'names')



class Game(models.Model):
	class Admin:
		pass
	def __str__(self):
		return self.name
	player_id = models.ForeignKey(Player)
	name = models.CharField(max_length=100)
	console = models.CharField(max_length=20)
	gender = models.CharField(max_length=10)
	language = models.CharField(max_length=10)
	desc_state = models.TextField()
