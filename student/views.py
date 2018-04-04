# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student,Request
from django.contrib.auth.decorators import login_required,user_passes_test #even after loging in the function only if he is certain user
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from random import randint
# Create your views here.

register = template.Library()

@login_required(login_url='/student/signin')	
def home1(request,param1='jess'): #to every function request is a parameter 
	print (param1)
	studentObjs = Student.objects.all().order_by('rollno')
	response ={} # making a dictionary named response to send all the parameters
	response['flag'] = False
	response['students'] = studentObjs
	#studentObjs = Student.objects.filter(full_name='student2')  # to get all the objects from student table filter:iterable get:notiterabled all:returns all 
	return render(request,'home.html',response) #by default it searches in the templates folders
	
@login_required(login_url='/student/signin')	
def home(request):
	response ={}
	current_user = request.user.username
	response['name'] = current_user
	return render(request,'production/index.html',response)
	#return redirect('\gentelella-master\production\index.html')

@login_required(login_url='/student/signin')	
def newreq(request):
	response ={}
	allUsers = User.objects.all()
	current_user = request.user.username
	response['name'] = current_user
	response['users'] = allUsers
	return render(request,'production/request.html',response)

@register.assignment_tag()
def random_no(length=3) :
		return randint(10**(length-1),(10**(length)-1))
		
def savereq(request):
	if request.method =="POST":
		type = request.POST['type']
		descrp = request.POST['message']
		touser = request.POST['to']
		check = random_no()
		while Request.objects.filter(rid=check):
			check = random_no()
		obj = Request()
		obj.rid=check
		obj.type=type
		obj.descrp=descrp
		obj.fromuser=request.user.username
		obj.touser = touser
		obj.save();
		
			
	return redirect('/student/index')	
	
@login_required(login_url='/student/signin')	
def saveData(request):
	if request.method =="POST":
		full_name = request.POST['full_name']
		rollno = request.POST['rollno']
		class_studying = request.POST['class_studying']
		father_name = request.POST['father_name']
		mother_name = request.POST['mother_name']
		father_phn = request.POST['father_phn']
		
		obj = Student()
		obj.full_name = full_name
		obj.rollno = rollno
		obj.class_studying = class_studying
		obj.father_name = father_name
		obj.mother_name = mother_name
		obj.father_phn = father_phn
		obj.save() #gets saved in the database
		
	return redirect('/student/home1')
	
def signin(request):
	response = {}
	if request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is None :
			return render(request,'login.html',response)
		else :
			login(request,user)
			return redirect('/student/index')
	return render(request,'login.html',response) #simply pressed login with no details redirect bakc
		
def logout_view(request):
    logout(request)
    return render(request,'login.html')		
 