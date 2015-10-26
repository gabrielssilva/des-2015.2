from django.db import models

# Create your models here.
class Transaction(models.Model):
	class Meta:
		abstract = True

	tipo = models.CharField(max_length = 30)
	data = models.DateTimeField()

class Advertisement(Transaction):
	disponibilidade = models.CharField(max_length=30)