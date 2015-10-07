from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Player(AbstractBaseUser):
	nome = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	senha = models.CharField(max_length=50)
	telefone = PhoneNumberField()

	USERNAME_FIELD = 'email'

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
