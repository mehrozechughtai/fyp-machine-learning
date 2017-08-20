# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MyClass(models.Model):
	"""docstring for MyClass"""
	text = models.CharField(max_length=500)

	def __str__(self):
		return self.text
	
