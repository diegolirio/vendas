# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from usuario.models import Usuario
from usuario.forms import UsuarioForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from usuario.forms import UserForm

# Create your views here.

def getAllUsuarios(request):
	usuarios = Usuario.objects.all()
	return render_to_response('usuarios.html', {'usuarios': usuarios}, context_instance=RequestContext(request))
		
#def getAllUsuarios(request):
#	users = Users.objects.all()
#	return render_to_response('usuarios.html', {'users': users}, context_instance=RequestContext(request))	

def new(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			#return getAllUsuarios(request)
			#return HttpResponseRedirect(reverse('usuario.views.getAllUsuarios'))			
			return HttpResponse('<h4>Usuario Cadastro com sucesso</h4><p><a href="/usuarios">Lista</a></p>')			
			#return HttpResponseRedirect(reverse('usuario.views.getAllUsuarios'))
			
			#return render_to_response('usuario_edit.html', 
			#                          {'form': form, 'msg': u'Usuário cadastro com sucesso!'}, 
			#                          context_instance=RequestContext(request))
	else:
		form = UsuarioForm()
	return render_to_response('usuario_new.html', {'form': form}, context_instance=RequestContext(request))
		
def edit(request, pk):
	usuario = Usuario.objects.get(pk=pk)
	msg = ""
	if request.method == 'POST':
		#return getAllUsuarios(request)
		#return HttpResponse('<h4>Usuario Cadastro com sucesso</h4><p><a href="/usuarios">Lista</a></p>')
		form = UsuarioForm(request.POST, request.FILES, instance=usuario)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect(reverse('usuario.views.getAllUsuarios'))
			return render_to_response('usuario_edit.html', 
			                          {'form': form, 'msg': u'Usuário cadastro com sucesso!'}, 
			                          context_instance=RequestContext(request))			
	else:
		form = UsuarioForm(instance=usuario)
	return render_to_response('usuario_edit.html', {'form': form, 'msg': msg}, context_instance=RequestContext(request))
	
def usuario_delete(request, pk):
	u = Usuario.objects.get(pk=pk)
	delected = 'N'
	if request.method == 'POST':
		u.delete()
		delected = 'S'
		#return getAllUsuarios(request)
		#return render_to_response('usuario_delete.html', )
	#else:
	return render_to_response('usuario_delete.html', {'usuario': u, 'delected': delected}, context_instance=RequestContext(request))



def users(request):
	users = User.objects.all()
	return render_to_response('users.html', {'users': users}, context_instance=RequestContext(request))	
	
def user_new(request):
	#user = User()
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return users(request)
	else:
		form = UserForm()
	return render_to_response('user_new.html', {'form': form}, context_instance=RequestContext(request))	

def user_edit(request, pk):
	user = User.objects.get(pk=pk)
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			return users(request)
	else:
		form = UserForm(instance=user)
	return render_to_response('user_edit.html', {'form': form}, context_instance=RequestContext(request))

def user_delete(request, pk):
	u = User.objects.get(pk=pk)
	delected = 'N'
	if request.method == 'POST': 
		u.delete()
		delected = 'S'
	return render_to_response('user_delete.html', {'user': u, 'delected': delected}, context_instance=RequestContext(request))
		
