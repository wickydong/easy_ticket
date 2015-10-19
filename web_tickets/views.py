#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from web_tickets.forms import LoginForm
from django.http import HttpResponseRedirect
from web_tickets.models import UserAuth
def index(request):
    return render_to_response("index.html") 


def login_form(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user_msg = UserAuth.objects.get(user=cd["user"])
                if str(user_msg.passwd) == cd["passwd"] and str(user_msg.god) == "yes":
                    print "Hi, Mr. %s, You Are Root!" % cd["user"]
                    return HttpResponseRedirect("/?a=b")
                elif str(user_msg.passwd) == cd["passwd"] and str(user_msg.god) == "no":
                    print "Hi, Mr. %s, You Are User!" % cd["user"]
                    return "Hi, Mr. %s, You Are User!" % cd["user"]
                else:
                    print "passwd wrong!"
                    return "passwd wrong!"
            except UserAuth.DoesNotExist:
                print "%s Not in db" % cd["user"]
                return "%s no exist" % cd["user"]
    else:
        form = LoginForm()
    return render_to_response("login.html",{"form": form},context_instance=RequestContext(request))
    #return render_to_response("login_form.html",{"user":user,"passwd":passwd})#,context_instance=RequestContext(request))


