from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:'),
    
    url(r'^$', 'vendas_produtos.views.home', name='home'),
    
    
    # Usuarios
    #url(r'^usuarios/$', 'usuario.views.getAllUsuarios', name='usuarios'),  
    #url(r'^usuario_new/$', 'usuario.views.new', name='new_user'),  
	#url(r'^usuario_edit/(?P<pk>\d+)/$', 'usuario.views.edit'),
	#url(r'^usuario_delete/(?P<pk>\d+)/$', 'usuario.views.usuario_delete'),
	
	# Users
	url(r'^users/$', 'usuario.views.users', name='users'),
	#url(r'^user_new/$', 'usuario.views.user_new'),
	#url(r'^user_edit/(?P<pk>\d+)/$', 'usuario.views.user_edit', name='user_edit'),
	#url(r'^user_delete/(?P<pk>\d+)/$', 'usuario.views.user_delete'),
	#url(r'^user_fotos/(?P<pk>\d+)/$', 'usuario.views.user_fotos'),
	url(r'^user_form/(?P<pk>\d+)/$', 'usuario.views.user_form'),
	
	# UsersPlus
	#url(r'^userPlus_edit/(?P<pk>\d+)/$', 'usuario.views.userPlus_edit'),
	#url(r'^userPlus_delete/(?P<pk>\d+)/$', 'usuario.views.userPlus_delete'),
	
	# ------ Clientes ------
    #url(r'^clientes/$', 'cliente.views.clientes', name='clientes'),  
	#url(r'^cliente_new/$', 'cliente.views.cliente_new'),
	#url(r'^cliente_edit/(?P<pk>\d+)/$', 'cliente.views.cliente_edit'),
	#url(r'^cliente_delete/(?P<pk>\d+)/$', 'cliente.views.cliente_delete'),
	
	# ------- Marcas ------
	url(r'^marcas/$', 'produto.views.marcas', name='marcas'),
	#url(r'^marca_new/$', 'produto.views.marca_new'),
	#url(r'^marca_edit/(?P<pk>\d+)/$', 'produto.views.marca_edit'),
	url(r'^marca_delete/(?P<pk>\d+)/$', 'produto.views.marca_delete'),
	url(r'^marca_form/(?P<pk>\d+)/$', 'produto.views.marca_form'),
	url(r'^marca_form_simple/(?P<pk>\d+)/$', 'produto.views.marca_form_simple'),
    
    # ------- Produtos ------
    url(r'^produtos/$', 'produto.views.produtos', name='produtos'),
    #url(r'^produto_new/$', 'produto.views.produto_new'),
    #url(r'^produto_edit/(?P<pk>\d+)/$', 'produto.views.produto_edit'),
    #url(r'^produto_delete/(?P<pk>\d+)/$', 'produto.views.produto_delete'),
    #url(r'^produto_fotos/(?P<pk>\d+)/$', 'produto.views.produto_fotos'),
    #url(r'^produto_fotos_form/$', 'produto.views.produto_fotos_form'),
    #url(r'^produto_foto_delete/$', 'produto.views.produto_foto_delete'),
    url(r'^produto_form/(?P<pk>\d+)/$', 'produto.views.produto_form'),
    
    # ------ Nfs ------
    #url(r'^nf_new/$', 'vendas_produtos.views.nf_new'),
    #url(r'^nf_det/(?P<pk>\d+)/$', 'vendas_produtos.views.nf_det'),
    #url(r'^nf_delete/(?P<pk>\d+)/$', 'vendas_produtos.views.nf_delete'),
    #url(r'^vendas_produtos/$', 'vendas_produtos.views.vendas', name='vendas'),
    
    #url(r'^nf_form2/(?P<pk>\d+)/$', 'vendas_produtos.views.nf_form2'),
    #url(r'^nf_form3/(?P<pk>\d+)/$', 'vendas_produtos.views.nf_form3'),
	#url(r'^nf_form4/(?P<pk>\d+)/$', 'vendas_produtos.views.nf_form4'),
    #url(r'^add_prod/(?P<pk>\d+)/$', 'vendas_produtos.views.add_prod'),
    #url(r'^nf_finalizar/(?P<pk>\d+)/$', 'vendas_produtos.views.nf_finalizar'),
    #url(r'^nf_print/(?P<pk>\d+)/$', 'vendas_produtos.views.nf_print'),
    #url(r'^nf_produto_delete/(?P<pk>\d+)/$', 'vendas_produtos.views.nf_produto_delete'),
    
    # url(r'^vendas/', include('vendas.foo.urls')),
    
    # ---------- Fornecedor ------------
    #url(r'^fornecedores/$', 'produto.views.fornecedores'),
    #url(r'^fornecedor_form/(?P<pk>\d+)/$', 'produto.views.fornecedor_form'),
    #url(r'^fornecedor_delete/(?P<pk>\d+)/$', 'produto.views.fornecedor_delete'),  
    
    # ---------- Tel -------------------
    #url(r'^tel_form/$', 'cliente.views.tel_form'),
    #url(r'^tel_delete/(?P<pk>\d+)/$', 'cliente.views.tel_delete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += patterns('', 
	                        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
