from django.shortcuts import render_to_response
from produto.models import Produto
from produto.models import Marca
from produto.forms import MarcaForm
from django.template import RequestContext

def produtos(request):
	
	ps = Produto.objects.all()
	
	return render_to_response('produtos.html', {'produtos': ps})
	
	
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
	
