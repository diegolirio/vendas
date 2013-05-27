from django.shortcuts import render_to_response
from django.shortcuts import redirect
from produto.models import Produto
from produto.models import FotoProduto
from produto.models import Marca
from produto.models import Fornecedor
from cliente.models import Telefone
from produto.forms import MarcaForm
from produto.forms import ProdutoForm
from produto.forms import FotoProdutoForm
from produto.forms import FornecedorForm
from django.template import RequestContext
from django.http import HttpResponseRedirect

INSERT = 'insert'
UPDATE = 'update'


def produtos(request):	
	ps = Produto.objects.all()	
	return render_to_response('produtos.html', {'produtos': ps})

def produto_new(request):
	if request.method == 'POST':
		form = ProdutoForm(request.POST, request.FILES)
		if form.is_valid():
			p = form.save()
			#return produtos(request)			
			return redirect('/produto_edit/'+str(p.pk))
	else:
		p = Produto()
		form = ProdutoForm(instance=p)
	return render_to_response('produto_new.html', {'form': form}, context_instance=RequestContext(request))
		
def produto_edit(request, pk):
	p = Produto.objects.get(pk=pk)
	try:
		foto_main = FotoProduto.objects.filter(produto=p, principal=True)[0:1].get()
	except:
		foto_main = None
	if request.method == 'POST':
		form = ProdutoForm(request.POST, request.FILES, instance=p)
		if form.is_valid():
			form.save()
			return produtos(request)
	else:
		form = ProdutoForm(instance=p)
	return render_to_response('produto_edit.html', {'form': form, 'produto': p, 'foto_main': foto_main}, context_instance=RequestContext(request)) 
		
def produto_delete(request, pk):
	p = Produto.objects.get(pk=pk)
	delected = 'N'
	if request.method == 'POST':
		p.delete()
		delected = 'S'
	return render_to_response('produto_delete.html', {'produto': p, 'delected': delected}, context_instance=RequestContext(request))
		
def produto_fotos(request, pk):
	#ToDO...: este methodo.... . Foto Somente Visualizacao...		
	p = Produto.objects.get(pk=pk)
	fotos = FotoProduto.objects.filter(produto=p).order_by('-principal')
	form = FotoProdutoForm()
	if request.method == 'POST':
		form = FotoProdutoForm(request.POST, request.FILES)
		if form.is_valid():
			if bool(form['principal'].value) == True:
				for f in fotos:
					f.principal = False
					f.save()
			form.save()
			form = FotoProdutoForm()
			fotos = FotoProduto.objects.filter(produto=p)
	return render_to_response('produto_fotos.html', {'produto': p, 'fotos': fotos, 'form': form}, context_instance=RequestContext(request))		
	
def produto_fotos_form(request):
	delected = 'N'
	# ToDo: Passar id produto por sessao...
	p = Produto.objects.get(pk=request.GET['produto_id'])
	if request.method == 'POST':
		if request.GET['foto_produto_id'] == '0':
			form = FotoProdutoForm(request.POST, request.FILES)
		if form.is_valid():
			delected = 'S'
			if bool(form['principal'].value) == True:
				fotos = FotoProduto.objects.filter(produto=p).order_by('-principal')
				for f in fotos:
					f.principal = False
					f.save()			
			form.save()
	else:
		if request.GET['foto_produto_id'] == '0':
			form = FotoProdutoForm()
		else:
			foto = FotoProduto.objects.get(pk=pk)
			form = FotoProdutoForm(instance=foto)
	return render_to_response('produto_fotos_form.html', {'form': form, 'delected': delected, 'produto': p}, context_instance=RequestContext(request))	
	
def marcas(request):
	marcas = Marca.objects.all()
	return render_to_response('marcas.html', {'marcas': marcas})	
	
	
def marca_new(request):
	if request.method == 'POST':
		form = MarcaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return marcas(request)
	else:
		form = MarcaForm()
	return render_to_response('marca_new.html', {'form': form}, context_instance=RequestContext(request))
	
	
def marca_edit(request, pk):
	m = Marca.objects.get(pk=pk)
	if request.method == 'POST':
		form = MarcaForm(request.POST, request.FILES, instance=m)
		if form.is_valid():
			form.save()
			return marcas(request)
	else:
		form = MarcaForm(instance=m)
	return render_to_response('marca_edit.html', {'form': form}, context_instance=RequestContext(request))	
	
	
def marca_delete(request, pk):
	m = Marca.objects.get(pk=pk)
	delected = 'N'
	if request.method == 'POST':
		m.delete()
		delected = 'S'
	return render_to_response('marca_delete.html', {'marca': m, 'delected': delected}, context_instance=RequestContext(request))
	
def fornecedores(request):
	fornecedores = Fornecedor.objects.all()
	return render_to_response('fornecedores.html', {'fornecedores': fornecedores})

def fornecedor_form(request, pk=None):
	f = Fornecedor()
	f.ie = ""
	if request.method == 'POST':
		if pk == '0':
			form = FornecedorForm(request.POST, request.FILES) 
		else:
			f = Fornecedor.objects.get(pk=pk)
			form = FornecedorForm(request.POST, request.FILES, instance=f) 			
		if form.is_valid():
			form.save()
			return fornecedores(request)
	else:
		if pk != '0':
			f = Fornecedor.objects.get(pk=pk)
		form = FornecedorForm()
	return render_to_response('fornecedor_form.html', 
	                          {'f': f, 'telefones': Telefone.objects.all(), 'form': form}, 
	                          context_instance=RequestContext(request))
	                          
def fornecedor_delete(request, pk):
	f = Fornecedor.objects.get(pk=pk)
	delected = 'N'
	if request.method == 'POST':
		f.delete()	                          
		delected = 'S'
	return render_to_response('fornecedor_delete.html', 
							  {'fornecedor': f, 'delected': delected, 'action': INSERT},
							  context_instance=RequestContext(request))
