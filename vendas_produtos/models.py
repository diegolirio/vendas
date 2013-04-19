from django.db import models
from cliente.models import Cliente
from produto.models import Produto

from django.contrib.auth.models import User

# Create your models here.

class NotaFiscal(models.Model):
	
	numero = models.IntegerField() 
	data = models.DateField()
	cliente = models.ForeignKey(Cliente)
	produtos =  models.ManyToManyField(Produto)
	#usuarioGerou =  models.ForeignKey(User)
	
	def __unicode__(self):
		return "NF: " + str(self.numero) + " - Data: " + str(self.data)

