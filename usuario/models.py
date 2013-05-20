from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import User
#from pessoa.models import Pessoa

# Create your models here.

class UserPlus(models.Model):
	
	#user = models.ForeignKey(User)
	#userPlus = models.ForeignKey(User)
	userPlus = models.ForeignKey(User, unique=True)
	foto = models.CharField(max_length=1000)

#class Usuario(Pessoa):
#	
#	login = models.CharField(max_length=10)
#	senha = models.CharField(max_length=10)
#	dataCadastro = models.DateTimeField()
#	
#	def __unicode__(self):
#		return self.login
		
	
