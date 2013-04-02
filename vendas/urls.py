from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:'),
    url(r'^clientes$', 'cliente.views.clientes', name='clientes'),
    url(r'^cad_cliente$', 'cliente.views.set_cliente', name='set_cliente'),
    url(r'^produtos$', 'produto.views.produtos', name='produtos'),
    url(r'^vendas_produtos$', 'vendas_produtos.views.vendas', name='vendas'),
    url(r'^$', 'vendas_produtos.views.home', name='home'),
    # url(r'^vendas/', include('vendas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)