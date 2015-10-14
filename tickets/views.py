#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response("index.html") 

def login(request):
    return render_to_response("login.html",context_instance=RequestContext(request))

def login_form(request):
    if request.method == "POST":
        user = request.POST["user"]
        passwd = request.POST["passwd"]
    return render_to_response("login_form.html",{"user":user,"passwd":passwd},context_instance=RequestContext(request))
