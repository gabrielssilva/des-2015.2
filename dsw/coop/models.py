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

	class Meta:
		verbose_name = (u'name')
		verbose_name_plural = (u'names')

	def __unicode__(self):
		return self.name
