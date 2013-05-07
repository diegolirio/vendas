# -*- coding: utf-8 -*-

from django.db import models
from cliente.models import Cliente
from produto.models import Produto

from django.contrib.auth.models import User

# Create your models here.


class NotaFiscal(models.Model):
	
	numero = models.IntegerField() 
	data = models.DateField()
	cliente = models.ForeignKey(Cliente)
	items = models.ManyToManyField(Produto, through='Items')
	#produtos =  models.ManyToManyField(Produto)
	#usuarioGerou =  models.ForeignKey(User)
	
	def __unicode__(self):
		return "NF: " + str(self.numero) + " - Data: " + str(self.data)

	def valorTotal(self):
		vlr = 0
		items = Items.objects.all().filter(nota=self)
		for it in items:
			vlr += (it.produto.valor * it.quantidade)
		return vlr


class Items(models.Model):
	nota = models.ForeignKey(NotaFiscal, related_name="nota")
	produto = models.ForeignKey(Produto, related_name="produto")
	quantidade = models.IntegerField() 
	 
	def __unicode__(self):
		return self.produto.nome + " - " + str(self.quantidade)
		
	def valorTotal(self):
		return self.produto.valor * self.quantidade
	
