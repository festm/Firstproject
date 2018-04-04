# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Fuser
from django.contrib.auth.decorators import login_required,user_passes_test #even after loging in the function only if he is certain user
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



def saveData(request):

	if request.method == "POST":
		cid = request.POST['spid']
		
	print(cid)

	if Fuser.objects.filter(fid=cid).exists():
		if Fuser.objects.filter(nop=0).exists() :
			fob=Fuser.objects.filter(fid=cid).update(nop=1)
 			return redirect(dispCred,cid)
		else:
			text="""<h1> Credentials already issued </h1>"""
			return HttpResponse(text)
	else:
		text="""<h2> Invalid ID </h2>"""
		return HttpResponse(text)

def dispCred(request,id):

	obj=Fuser.objects.filter(fid=id)
	resp={}
	resp['flag']=False
	resp['fusers']=obj
	return render(request, 'cred.html',resp)


def fourdig(request):
#need to write code to check if first time

	return render(request, 'start.html')

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
	
def savereq(request):
	if request.method =="POST":
		type = request.POST['type']
		descrp = request.POST['message']
		totype = request.POST['to']
		print(type)
		print(descrp)
		print(touser)
		
			
	return render(request,'production/index.html')	
	

	
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
 