from django.db import models
from coop.models import Player
from datetime import datetime
from dsw import settings


class Game(models.Model):
	def __str__(self):
		return self.nome

	player_id = models.ForeignKey(settings.AUTH_USER_MODEL)
	nome = models.CharField(max_length=100)
	console = models.CharField(max_length=20)
	genero = models.CharField(max_length=30)
	linguagem = models.CharField(max_length=10)
	estado = models.TextField()


class Transaction(models.Model):
	class Meta:
		abstract = True

	tipo = models.CharField(max_length = 30)
	data = models.DateTimeField()
	games = models.ManyToManyField(Game)


class Advertisement(Transaction):
	disponibilidade = models.CharField(max_length=30)
