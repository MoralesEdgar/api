# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class archivo(models.Model):
	autor 	          = models.ForeignKey(User)
	nombre_archivo    = models.CharField(max_length=200)
	archivo           = models.FileField(upload_to='data')
	create_at         = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nombre_archivo
