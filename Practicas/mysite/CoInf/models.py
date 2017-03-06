from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Departaments(models.Model):
	"""docstring for Missatges"""
	nom=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	"""incidencia=models.CharField(max_length=120)"""
	"""usuaris=models.ManyToManyField(Usuaris)"""
	def __str__(self):
		return self.nom

class Usuaris(models.Model):
	"""docstring for Login"""
	nom=models.CharField(max_length=20)
	cognoms=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	tipus=models.CharField(max_length=20)
	departament=models.ManyToManyField(Departaments)
	contrasenya=models.CharField(max_length=64)
	def __str__(self):
		return self.nom

class Incidencies(models.Model):
	"""docstring for Hashtags"""
	"""identificador=models.IntegerField(default=0)"""
	"""departament=models.ForeignKey(Departaments)"""
	nom=models.CharField(max_length=50, default='')
	departament=models.ManyToManyField(Departaments)
	estat=models.CharField(max_length=20)
	descripcion=models.CharField(max_length=200,default='')
	
	def __str__(self):
		return self.nom


class Material(models.Model):
	"""docstring for Hashtags"""
	nom=models.CharField(max_length=20)
	quantitat=models.IntegerField(default=0)
	"""idcompras=models.ForeignKey(Compres,related_name='+')"""
	"""idcompras=models.ManyToManyField(Compres)"""
	caracteristiques=models.CharField(max_length=120)
	
	def __str__(self):
		return self.nom

class Compres(models.Model):
	"""docstring for Hashtags"""
	"""identificador=models.IntegerField(default=0)"""
	numero=models.IntegerField(default=0)
	"""departament=models.ForeignKey(Departaments)"""
	departament=models.ManyToManyField(Departaments)
	material=models.ForeignKey(Material,default='')
	quantitat=models.IntegerField(default=1)
	
	def __str__(self):
		return str(self.numero)