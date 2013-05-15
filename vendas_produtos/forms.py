from django import forms
from django.forms import ModelForm
from vendas_produtos.models import *

class NFForm(forms.Form):
	numero = models.IntegerField()   
	cliente = models.ForeignKey(Cliente) 
	data = forms.DateField( widget=forms.DateInput(format='d%/%m/%Y'), input_formats=['%d/%m/%Y','%d/%m/%y'])	

class NotaFiscalForm(ModelForm):
	class Meta:
		model = NotaFiscal	
		
class ItemsForm(ModelForm):
	class Meta:
		model = Items
		
		
