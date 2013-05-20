from django.forms import ModelForm
#from usuario.models import Usuario
from usuario.models import UserPlus

from django.contrib.auth.models import User

#class UsuarioForm(ModelForm):
#	class Meta:
#		model = Usuario

class UserForm(ModelForm):
	class Meta:
		model = User

class UserPlusForm(ModelForm):
	class Meta:
		model = UserPlus
