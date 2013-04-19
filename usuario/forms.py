from django.forms import ModelForm
from usuario.models import Usuario

from django.contrib.auth.models import User

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario

class UserForm(ModelForm):
	class Meta:
		model = User
