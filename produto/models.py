from django.db import models

# Create your models here.

class Marca(models.Model):
	
	nome = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.nome

class Produto(models.Model):
	
	codigo = models.IntegerField()
	nome  = models.CharField(max_length=50)
	valor = models.FloatField()
	data_compra = models.DateField()
	marca = models.ForeignKey(Marca)
	
	def __unicode__(self):
		return str(self.codigo) + ": " + self.nome + " - " + self.marca.nome
	
