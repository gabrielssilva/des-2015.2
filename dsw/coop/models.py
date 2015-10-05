from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
	class Admin:
		pass
	def __str__(self):
		return self.email
	nome = models.CharField(max_length=100)
	email = models.EmailField()
	senha = models.CharField(max_length=50)
	telefone = PhoneNumberField()

	class Meta:
		verbose_name = (u'name')
		verbose_name_plural = (u'names')

	def __unicode__(self):
		return self.name


class Game(models.Model):
	class Admin:
		pass
	def __str__(self):
		return self.name
	user_id = models.ForeignKey(User)
	name = models.CharField(max_length=100)
	console = models.CharField(max_length=20)
	gender = models.CharField(max_length=10)
	language = models.CharField(max_length=10)
	desc_state = models.TextField()
