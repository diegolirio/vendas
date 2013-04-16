from django.forms import ModelForm
from produto.models import Marca
from produto.models import Produto

#class MarcaForm(forms.ModelForm):
class MarcaForm(ModelForm):
	class Meta:
		model = Marca
		
class ProdutoForm(ModelForm):
	class Meta:
		model = Produto		
