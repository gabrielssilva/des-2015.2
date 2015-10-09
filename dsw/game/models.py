from django.db import models
from coop.models import Player
from datetime import datetime


class Transaction(models.Model):
	class Meta:
		abstract = True

	tipo = models.CharField(max_length = 30)
	data = models.DateTimeField()

class Advertisement(Transaction):
	disponibilidade = models.CharField(max_length=30)


class Game(models.Model):
	def __str__(self):
		return self.name

	player_id = models.ForeignKey(Player)
	nome = models.CharField(max_length=100)
	console = models.CharField(max_length=20)
	genero = models.CharField(max_length=30)
	linguagem = models.CharField(max_length=10)
	estado = models.TextField()
