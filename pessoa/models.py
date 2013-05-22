from django.db import models

# Create your models here.

class Pessoa(models.Model):
	class Meta:
		abstract = True
		
	nome = models.CharField(max_length=50)
