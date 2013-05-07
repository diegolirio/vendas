from django.forms import ModelForm
from vendas_produtos.models import *

class NotaFiscalForm(ModelForm):
	class Meta:
		model = NotaFiscal
		
class ItemsForm(ModelForm):
	class Meta:
		model = Items
		
		
