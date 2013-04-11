from django.shortcuts import render_to_response
from usuario.models import Usuario
from usuario.forms import UsuarioForm

# Create your views here.

def getAllUsuarios(request):
	usuarios = Usuario.objects.all()
	return render_to_response('usuarios.html', {'usuarios': usuarios})

def new(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return getAllUsuarios(request)
			#return HttpResponseRedirect(reverse('usuario.views.getAllUsuarios'))
	else:
		u = Usuario()
		form = UsuarioForm(instance=u)
		return render_to_response('usuario_new.html', {'form': form})
		
def edit(request, pk):
	if request.method == 'POST':
		return getAllUsuarios(request)
	else:
		usuario = Usuario.objects.get(pk=pk)
		form = UsuarioForm(instance=usuario)
		return render_to_response('usuario_edit.html', {'form': form})		
