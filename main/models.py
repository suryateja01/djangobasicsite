from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=200)
	mobile = models.CharField(max_length=10, null=True)
	email = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.username


class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	country = models.CharField(max_length=200 )
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name
