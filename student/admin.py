# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student,Teacher,Request 

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Request)