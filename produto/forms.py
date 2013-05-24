from django.forms import ModelForm
from produto.models import Marca
from produto.models import Produto
from produto.models import FotoProduto
from produto.models import Fornecedor

#class MarcaForm(forms.ModelForm):
class MarcaForm(ModelForm):
	class Meta:
		model = Marca
		
class ProdutoForm(ModelForm):
	class Meta:
		model = Produto		

class FornecedorForm(ModelForm):
	class Meta:
		model = Fornecedor
		
class FotoProdutoForm(ModelForm):
	class Meta:
		model = FotoProduto
