from django.forms import ModelForm
from produto.models import Marca

#class MarcaForm(forms.ModelForm):
class MarcaForm(ModelForm):
	class Meta:
		model = Marca
