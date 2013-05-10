from django.shortcuts import render_to_response
from vendas_produtos.models import NotaFiscal
from vendas_produtos.models import Items
from cliente.models import Cliente
from cliente.models import Telefone
from produto.models import Produto
from produto.models import Marca
from vendas_produtos.forms import NotaFiscalForm
from django.template import RequestContext

def home(request):
	return render_to_response('index.html')

def vendas(request):	
	nfs = NotaFiscal.objects.all()	
	return render_to_response('vendas.html', {'nfs': nfs})

def nf_new(request):
	if request.method == 'POST':
		form = NotaFiscalForm(request.POST, request.FILES)
		if form.is_valid():
			model = form.save()
			#nf = NotaFiscal.objects.get(pk=model.id)
			return nf_det(request, model.id) #render_to_response('nf_det.html', {'form': form, 'nf': nf}, context_instance=RequestContext(request))
	else:
		nf = NotaFiscal()
		form = NotaFiscalForm(instance=nf)
	return render_to_response('nf_new.html', {'form': form}, context_instance=RequestContext(request))

def nf_det(request, pk):
	nf = NotaFiscal.objects.get(pk=pk)
	items = Items.objects.all().filter(nota=nf)
	return render_to_response('nf_det.html', {'nf': nf, 'items': items})
 
def nf_delete(request, pk):
	nf = NotaFiscal.objects.get(pk=pk)
	delected = 'N'
	if request.method == 'POST':
		nf.delete()
		delected = 'S'	
	return render_to_response('nf_delete.html', {'nf': nf, 'delected': delected}, context_instance=RequestContext(request))
	
def nf_form(request, pk):
	if request.method == 'POST':
		return vendas(request)
	else:
		nf = NotaFiscal()
	return render_to_response('nf_form.html',{'nf':nf}, context_instance=RequestContext(request))
	
	
