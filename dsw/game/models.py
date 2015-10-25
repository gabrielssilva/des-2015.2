from django.db import models
from coop.models import Player
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
