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
	description = models.CharField(max_length=4000, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Country(models.Model):
	code = models.CharField(max_length=2) #eg: US
	description = models.CharField(max_length=50) # United States of America
	currrencycode = models.CharField(max_length=15) #USD
	conversionrate = models.FloatField() # 1