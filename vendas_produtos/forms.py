from django.forms import ModelForm
from vendas_produtos.models import NotaFiscal

class NotaFiscalForm(ModelForm):
	class Meta:
		model = NotaFiscal
