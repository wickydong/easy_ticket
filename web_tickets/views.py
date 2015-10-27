#! /usr/bin/python
# -*- coding: utf-8 -*-
# __author__: wickydong

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from web_tickets.models import UserAuth,Tickets
from web_tickets.forms import LoginForm,ServerForm,UpgradeForm,VirtualForm,UpdateForm,FixForm


def index(request):
    return render_to_response("index.html") 


def login_form(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user_msg = UserAuth.objects.get(user=cd["user"])
                if str(user_msg.passwd) == cd["passwd"]:
                    request.session["user"] = cd["user"]
                    request.session["god"] = str(user_msg.god)
                    request.session["status"] = True
                    return HttpResponseRedirect("/my_tickets/")
            except UserAuth.DoesNotExist:
                print "Message Is DoesNotExist"
    else:
        #if request.session.get("status",False):   #用户已登录则跳转,上线需开启
        #    return HttpResponseRedirect("/my_tickets/")
        form = LoginForm()
    return render_to_response("login.html",{"form": form},\
                  context_instance=RequestContext(request))

def my_tickets(request):
   if request.session.get("status",False):
        user_title = request.session.get("god")
        if request.method == "POST":      #GET请求展示工单,POST请求处理工单
            if user_title == "yes":
                pass
            else:
                pass
        else:
            if user_title == "yes":
                tickets = Tickets.objects.filter(tks_status="nyet")
            else:
                tickets = Tickets.objects.filter(user=request.session.get("user"))
            return render_to_response("my_tickets.html",{"tickets": tickets})

def tickets(request,t_type):
    if request.session.get("status",False) and request.method == "GET":
        try:
            t_type = str(t_type)
        except ValueError:
            raise Http404()
        if t_type == "server":
            form = ServerForm()
        if t_type == "upgrade":
            form = UpgradeForm()
        if t_type == "virtual":
            form = VirtualForm()
        if t_type == "update":
            form = UpdateForm()
        if t_type == "fix":
            form = FixForm()
        return render_to_response("send_tickets.html",{"form":form},\
                                   context_instance=RequestContext(request))





            
         
    
