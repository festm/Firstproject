from django.conf.urls import url
from . import views

urlpatterns = [
	
        url(r'^home/(?P<param1>[A-Za-z0-9.-_]+)/$', views.home),  #param1 is the parameter type of values that acceptable + means more than one character[0-9](6). it is mandatory to send url
	url(r'^savereq/$',views.savereq),
	url(r'^signin/$',views.signin),
	url(r'^index/$',views.home,name="index"),
	url(r'^logout/$',views.logout_view,name="logout"),
	url(r'^createrequest/$',views.newreq,name="createreq"),
        url(r'^start/', views.fourdig),
        url(r'^saveData/$', views.saveData),
        url(r'^cred/$',views.dispCred),
        url(r'^cred/(?P<id>[A-Za-z0-9.,]+)/$',views.dispCred),
]