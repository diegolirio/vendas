from django.forms import ModelForm
from usuario.models import Usuario

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario
