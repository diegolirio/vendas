from django.shortcuts import render_to_response
from produto.models import Produto
from produto.models import Marca

def produtos(request):
	
	ps = Produto.objects.all()
	
	return render_to_response('produtos.html', {'produtos': ps})

# Create your views here.
