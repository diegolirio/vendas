from django.shortcuts import render_to_response
from cliente.models import Cliente
from cliente.models import Telefone
from django import forms

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        #fields = ['id', 'cnpj_cpf', 'telefone.ddd/numero']

def clientes(request):	
	clientes = Cliente.objects.all()	
	return render_to_response('clientes.html', {'clientes': clientes})	
	
	
def set_cliente(request):
	return render_to_response('cad_cliente.html')	
	
	
def cliente_edit(request, pk=None):	
	if request.method == 'POST':
		form = ClienteForm(request.POST, request.FILES)  
		if form.is_valid():
			c = form.save(commit=False)
			c.save()
			
			return clientes(request)
	else:
		c = Cliente.objects.get(pk=pk)
		form = ClienteForm(instance=c)
		return render_to_response('cliente_edit.html', {'c':c, 'form': form})		
