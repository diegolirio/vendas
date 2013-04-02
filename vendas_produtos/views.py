from django.shortcuts import render_to_response
from vendas_produtos.models import NotaFiscal
from cliente.models import Cliente
from cliente.models import Telefone
from produto.models import Produto
from produto.models import Marca

def home(request):
	return render_to_response('index.html')

def vendas(request):
	
	nfs = NotaFiscal.objects.all()
	
	return render_to_response('vendas.html', {'nfs': nfs})

