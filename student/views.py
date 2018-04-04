# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User

from .models import Fuser,Request
from django.contrib.auth.decorators import login_required,user_passes_test #even after loging in the function only if he is certain user
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from random import randint


register = template.Library()

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
 