from django.db import models
from django.db.models.base import Model

# Create your models here.
class List(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	