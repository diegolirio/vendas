from django.contrib import admin
from produto.models import Marca
from produto.models import Produto
from produto.models import Fornecedor

admin.site.register(Marca)
admin.site.register(Produto)
admin.site.register(Fornecedor)
