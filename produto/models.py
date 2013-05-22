from django.db import models
from cliente.models import Telefone

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
	

class Fornecedor(models.Model):
	cnpj_cpf = models.CharField(max_length=20)
	nome = models.CharField(max_length=50)
	telefone = models.ForeignKey(Telefone) 
	ie = models.IntegerField()
	
	# Erro ao Salvar...
	#def __init__(self):
		#self.ie = ""	
	
	def __unicode__(self):
		return self.nome
