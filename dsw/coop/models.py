from django.db import models

# Create your models here.

class User(models.Model):
	class Admin:
		pass
	def __str__(self):
		return self.email
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

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
