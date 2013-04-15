from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:'),
    
    # Usuarios
    url(r'^usuarios/$', 'usuario.views.getAllUsuarios', name='usuarios'),  
    url(r'^usuario_new/$', 'usuario.views.new', name='new_user'),  
	url(r'^usuario_edit/(?P<pk>\d+)/$', 'usuario.views.edit'),
	url(r'^usuario_delete/(?P<pk>\d+)/$', 'usuario.views.usuario_delete'),
	
	# ------ Clientes ------
    url(r'^clientes/$', 'cliente.views.clientes', name='clientes'),  
	url(r'^cliente_new/$', 'cliente.views.cliente_new'),
	url(r'^cliente_edit/(?P<pk>\d+)/$', 'cliente.views.cliente_edit'),
	url(r'^cliente_delete/(?P<pk>\d+)/$', 'cliente.views.cliente_delete'),
	
	# ------- Marcas ------
	url(r'^marcas/$', 'produto.views.marcas'),
	url(r'^marca_new/$', 'produto.views.marca_new'),
	url(r'^marca_edit/(?P<pk>\d+)/$', 'produto.views.marca_edit'),
	url(r'^marca_delete/(?P<pk>\d+)/$', 'produto.views.marca_delete'),
    
    url(r'^produtos/$', 'produto.views.produtos', name='produtos'),
    url(r'^vendas_produtos/$', 'vendas_produtos.views.vendas', name='vendas'),
    url(r'^$', 'vendas_produtos.views.home', name='home'),
    # url(r'^vendas/', include('vendas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += patterns('', 
	                        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
