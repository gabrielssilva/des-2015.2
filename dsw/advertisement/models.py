from django.db import models
from game.models import Game

# Create your models here.
class Transaction(models.Model):
    class Meta:
        abstract = True

    tipo = models.CharField(max_length = 30)
    data = models.DateTimeField()
    games = models.ManyToManyField(Game)


class Advertisement(Transaction):
    disponibilidade = models.CharField(max_length=30)