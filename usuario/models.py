from django.db import models
from pessoa.models import Pessoa

# Create your models here.

class Usuario(Pessoa):
	
	login = models.CharField(max_length=10)
	senha = models.CharField(max_length=10)
	dataCadastro = models.DateTimeField()
	
	def __unicode__(self):
		return self.login
		
	
