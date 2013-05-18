from django.shortcuts import render_to_response
from vendas_produtos.models import NotaFiscal
from vendas_produtos.models import Items
from cliente.models import Cliente
from cliente.models import Telefone
from produto.models import Produto
from produto.models import Marca
from vendas_produtos.forms import NotaFiscalForm
from vendas_produtos.forms import NFForm
from vendas_produtos.forms import NFForm2
from vendas_produtos.forms import ItemsForm
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
	nf = NotaFiscal()
	nf.numero = ""
	nf.data = ""
	clientes = Cliente.objects.all()
	if request.method == 'POST':
		return vendas(request)
	else:
		if pk != '0':
			nf = NotaFiscal.objects.get(pk=pk)
	return render_to_response('nf_form.html',{'nf':nf, 'clientes': clientes}, context_instance=RequestContext(request))
	
def nf_form2(request, pk):
	nf = NotaFiscal()
	clientes = Cliente.objects.all()
	if request.method == 'POST':
		if pk != '0':
			nf = NotaFiscal.objects.get(pk=pk)
			form = NotaFiscalForm(request.POST, request.FILES, instance=nf)
		else:
			form = NotaFiscalForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			print('NF gravada com sucesso')
			return vendas(request)
		else:
			print('form invalido')
	else:
		form = NotaFiscalForm()
	return render_to_response('nf_form2.html', {'nf': nf, 'clientes': clientes, 'form': form}, context_instance=RequestContext(request))
	
def nf_form3(request, pk):
	nf = NotaFiscal()
	clientes = Cliente.objects.all()
	if request.method == 'POST':
		if pk != '0':
			nf = NotaFiscal.objects.get(pk=pk)
			form = NFForm(request.POST, request.FILES, instance=nf)
		else:
			form = NFForm(request.POST, request.FILES)
		if form.is_valid():
			dados = form.cleaned_data
			nf = NotaFiscal(
								numero=dados['numero'],
								data=dados['data'],
								cliente=dados['cliente']
							)
			#form.save()
			nf.save()
			return vendas(request)
	else:
		form = NFForm()
	return render_to_response('nf_form3.html', 
	                          {'nf':nf, 'clientes':clientes, 'form':form}, 
	                          context_instance=RequestContext(request))
	                          
# ============================================================================#
# = Form4 - Oficial															  #	                          
# ============================================================================#
def nf_form4(request, pk):		
	if request.method == 'POST':
		if pk != '0':
			nf = NotaFiscal.objects.get(pk=pk)
			items = Items.objects.all().filter(nota=nf)
			form = NFForm2(request.POST, request.FILES, instance=nf)
		else:
			items = False
			form = NFForm2(request.POST, request.FILES)
		if form.is_valid():
			nf_form = form.save()
			return nf_det(request, nf_form.pk)
	else:
		if pk != '0':	
			nf = NotaFiscal.objects.get(pk=pk)
			items = Items.objects.all().filter(nota=nf)
			form = NFForm2(instance=nf)
		else:
			items = False		
			form = NFForm2()
	return render_to_response('nf_form4.html', {'form':form, 'items': items}, context_instance=RequestContext(request))

def add_prod(request, pk):
	nf = NotaFiscal.objects.get(pk=pk)
	delected = 'N'
	if request.method == 'POST':
		form = ItemsForm(request.POST, request.FILES)
		if form.is_valid(): 
			form.save()
			delected = 'S'
	else:
		form = ItemsForm(instance=nf)
	return render_to_response('nf_add_prod.html', 
	                          {'nf': nf, 'form': form, 'delected': delected}, 
	                          context_instance=RequestContext(request))
