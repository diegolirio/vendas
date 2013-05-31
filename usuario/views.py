# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.shortcuts import redirect
#from usuario.models import Usuario
from usuario.models import UserPlus
#from usuario.forms import UsuarioForm
from usuario.forms import UserPlusForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from usuario.forms import UserForm

# Create your views here.

#def getAllUsuarios(request):
#	usuarios = Usuario.objects.all()
#	return render_to_response('usuarios.html', {'usuarios': usuarios}, context_instance=RequestContext(request))
		
#def getAllUsuarios(request):
#	users = Users.objects.all()
#	return render_to_response('usuarios.html', {'users': users}, context_instance=RequestContext(request))	

#def new(request):
#	if request.method == 'POST':
#		form = UsuarioForm(request.POST, request.FILES)
#		if form.is_valid():
#			form.save()
			#return getAllUsuarios(request)
			#return HttpResponseRedirect(reverse('usuario.views.getAllUsuarios'))			
#			return HttpResponse('<h4>Usuario Cadastro com sucesso</h4><p><a href="/usuarios">Lista</a></p>')			
			#return HttpResponseRedirect(reverse('usuario.views.getAllUsuarios'))
			
			#return render_to_response('usuario_edit.html', 
			#                          {'form': form, 'msg': u'Usuário cadastro com sucesso!'}, 
			#                          context_instance=RequestContext(request))
#	else:
#		form = UsuarioForm()
#	return render_to_response('usuario_new.html', {'form': form}, context_instance=RequestContext(request))
		
#def edit(request, pk):
#	usuario = Usuario.objects.get(pk=pk)
#	msg = ""
#	if request.method == 'POST':
		#return getAllUsuarios(request)
		#return HttpResponse('<h4>Usuario Cadastro com sucesso</h4><p><a href="/usuarios">Lista</a></p>')
#		form = UsuarioForm(request.POST, request.FILES, instance=usuario)
#		if form.is_valid():
#			form.save()
			#return HttpResponseRedirect(reverse('usuario.views.getAllUsuarios'))
#			return render_to_response('usuario_edit.html', 
#			                          {'form': form, 'msg': u'Usuário cadastro com sucesso!'}, 
#			                          context_instance=RequestContext(request))			
#	else:
#		form = UsuarioForm(instance=usuario)
#	return render_to_response('usuario_edit.html', {'form': form, 'msg': msg}, context_instance=RequestContext(request))
	
#def usuario_delete(request, pk):
#	u = Usuario.objects.get(pk=pk)
#	delected = 'N'
#	if request.method == 'POST':
#		u.delete()
#		delected = 'S'
#		#return getAllUsuarios(request)
#		#return render_to_response('usuario_delete.html', )
#	#else:
#	return render_to_response('usuario_delete.html', {'usuario': u, 'delected': delected}, context_instance=RequestContext(request))



def users(request):
	users = User.objects.all()
	return render_to_response('_base.html', {'users': users, 'template': 'users.html'}, context_instance=RequestContext(request))	
	
def user_form(request, pk):
	u = User()		
	userPlus = UserPlus()
	form = UserForm()
	if pk != '0':
		u = User.objects.get(pk=pk)
		form = UserForm(instance=u)
		try:
			userPlus = UserPlus.objects.get(user=user)
		except:
			userPlus = UserPlus()		
	if request.method == 'POST':
		if pk != '0':
			form = UserForm(request.POST, request.FILES, instance=u)
		else:
			form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('users')	
	return render_to_response('_base.html', 
	                          {  'form': form, 
	                             'user': u, 
	                             'template': 
	                             'user_form.html', 
	                             'userPlus': userPlus }, 
	                          context_instance=RequestContext(request))
	
#def user_new(request):
#	#user = User()
#	if request.method == 'POST':
#		form = UserForm(request.POST, request.FILES)
#		if form.is_valid():
#			form.save()
#			return redirect('users')
#	else:
#		form = UserForm()
#	return render_to_response('user_new.html', {'form': form}, context_instance=RequestContext(request))	

#def user_edit(request, pk):
#	user = User.objects.get(pk=pk)
#	userPlus = UserPlus()
#	try:
#		userPlus = UserPlus.objects.get(user=user)
#	except:
#		userPlus = UserPlus()
#	if request.method == 'POST':
#		form = UserForm(request.POST, request.FILES, instance=user)
#		if form.is_valid():
#			form.save()
#			return redirect('users')
#	else:
#		form = UserForm(instance=user)
#	return render_to_response('user_edit.html', {'form': form, 'user': user, 'userPlus': userPlus}, context_instance=RequestContext(request))

#def user_delete(request, pk):
#	u = User.objects.get(pk=pk)
#	delected = 'N'
#	if request.method == 'POST': 
#		u.delete()
#		delected = 'S'
#	return render_to_response('user_delete.html', {'user': u, 'delected': delected}, context_instance=RequestContext(request))

#def userPlus_edit(request, pk):
#	#userPlus = UserPlus.objects.get(pk=pk)
#	user = User.objects.get(pk=pk)
#	try:
#		userPlus = UserPlus.objects.get(user=user)
#	except:
#		userPlus = UserPlus()
#	#print("Foto >>>>>" + userPlus.foto.url)
##		#if userPlus.foto == 
	#	try:
	#		if userPlus.pk > 0:
	#			form = UserPlusForm(request.POST, request.FILES, instance=userPlus)
	#		else:
	#			form = UserPlusForm(request.POST, request.FILES)
	#	except:
	#		form = UserPlusForm(request.POST, request.FILES)				
	#	if form.is_valid():
	#		form.save() 
	#		return redirect('user_edit', pk=user.pk)
	#else:
	#	if userPlus.pk > 0:
	#		form = UserPlusForm(instance=userPlus)
	#	else:
	#		form = UserPlusForm()
	#return render_to_response('user_edit.html', {'form': form, 'foto': 'S', 'userPlus': userPlus}, context_instance=RequestContext(request))

#def userPlus_delete(request, pk):
#	u = UserPlus.objects.get(pk=pk)
#	user = u.user
#	#delected = 'N'
#	#if request.method == 'POST': 
#	u.delete()
#	
#	form = UserPlusForm()
#	userPlus = UserPlus()
#	#	delected = 'S'
#	#return render_to_response('user_delete.html', {'user': u, 'foto': 'S', 'delected': delected}, context_instance=RequestContext(request))	
#	return render_to_response('user_edit.html', {'form': form, 'foto': 'S', 'userPlus': userPlus}, context_instance=RequestContext(request))
		
#def user_fotos(request, pk):
#	user = User.objects.get(pk=pk)
#	#usersPlus = UserPlus.objects.get(user=user)
#	usersPlus = UserPlus.objects.filter(user=user)
#	return render_to_response('user_fotos.html',{'usersPlus': usersPlus, 'user': user})
