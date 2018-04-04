# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Teacher(models.Model):
	name = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	contact = models.CharField(max_length=255)
	
	def __str__(self): 
		return str(self.name)
		
class Student(models.Model):
	class_studying = models.CharField(max_length=255)
	rollno = models.IntegerField(null=True) #can create student with no roll number
	full_name = models.CharField(max_length=255)
	father_name = models.CharField(max_length=255 ,blank=True)
	father_phn = models.CharField(max_length=255 ,blank=True)
	mother_name = models.CharField(max_length=255 ,blank=True)
	teacher = models.ForeignKey(Teacher,null=True) # as we already have data put null=true
	
	def __str__(self) :
	    return str(self.full_name)
		
class Request(models.Model):
	rid = models.IntegerField(null=False)
	Type = models.CharField(max_length=1)
	descrp = models.CharField(max_length=255 ,null=True) 
	fromuser =  models.CharField(max_length=255 ,null=False)
	touser = models.CharField(max_length=255 ,null=False)
	
	def __str__(self) :
	    return str(self.rid)

		
