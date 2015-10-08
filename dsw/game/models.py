from django.db import models
from coop.models import Player
class Game(models.Model):
	class Admin:
		pass
	def __str__(self):
		return self.name
	user_id = models.ForeignKey(Player)
	name = models.CharField(max_length=100)
	console = models.CharField(max_length=20)
	gender = models.CharField(max_length=10)
	language = models.CharField(max_length=10)
	desc_state = models.TextField()

