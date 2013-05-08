from django.db import models

# Create your models here.

class Telefone(models.Model):
	
	ddd = models.IntegerField(max_length=2)
	numero = models.IntegerField(max_length=10)
	
	def __unicode__(self):
		return "(" + str(self.ddd) + ") " + str(self.numero) 

class Pessoa(models.Model):
	class Meta:
		abstract = True
		
	nome = models.CharField(max_length=50)
	telefone = models.ForeignKey(Telefone)

class Cliente(Pessoa):
	
	cnpj_cpf = models.CharField(max_length=14)
	
	def __unicode__(self):
		return self.nome + " (" + self.cnpj_cpf + ")"
	
	
