# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from cliente.models import Cliente
from cliente.models import Telefone
from django import forms
from django.http import HttpResponse
from django.template import RequestContext

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        #fields = ['id', 'cnpj_cpf', 'telefone.ddd/numero']

def clientes(request):	
	clientes = Cliente.objects.all()	
	return render_to_response('clientes.html', {'clientes': clientes})	
		
def cliente_new(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			
			return HttpResponse('<h1>Cliente cadastrado com sucesso</h1><p><a href="/clientes/">Voltar</a></p>') 
	else:
		c = Cliente()
		form = ClienteForm(instance=c)
	return render_to_response('cliente_new.html', {'form': form}, context_instance=RequestContext(request))	
	
	
def cliente_edit(request, pk=None):	
	c = Cliente.objects.get(pk=pk)
	if request.method == 'POST':
		form = ClienteForm(request.POST, request.FILES, instance=c)  
		if form.is_valid():
			form.save()
			#return clientes(request)
			return HttpResponse('<h1>Cliente ' + c.nome + ' alterado com sucesso</h1><p><a href="/clientes/">Voltar</a></p>')
	else:
		form = ClienteForm(instance=c)
	return render_to_response('cliente_edit.html', {'c':c, 'form': form}, context_instance=RequestContext(request))		
	
def cliente_delete(request, pk):
	c = Cliente.objects.get(pk=pk)
	if request.method == 'POST':
		c.delete()
		return clientes(request)
	else:			
		return render_to_response('cliente_delete.html', {'cliente': c}, context_instance=RequestContext(request))
