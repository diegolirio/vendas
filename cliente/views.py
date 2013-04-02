from django.shortcuts import render_to_response
from cliente.models import Cliente
from cliente.models import Telefone

def clientes(request):
	
	clientes = Cliente.objects.all()
	
	return render_to_response('clientes.html', {'clientes': clientes})	
	
def set_cliente(request):
	return render_to_response('cad_cliente.html')	
