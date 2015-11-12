#! /usr/bin/python
# -*- coding: utf-8 -*-
# __author__: wickydong

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from web_tickets.models import *
from web_tickets.forms import *
import md5,datetime

def makemd5(msg):
    make = md5.new()
    make.update(msg)
    return make.hexdigest()
def now():
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print now
    return now

def index(request):
    #if request.session.get("status",False):   #用户已登录则跳转,上线需开启
    #    return HttpResponseRedirect("/my_tickets/")
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
        user = request.session.get("user")
        if request.method == "POST":      #GET请求展示工单,POST请求处理工单
            return HttpResponseRedirect("/")
        else:
            server = AllForm.objects.filter(make_user=user)
            return render_to_response("my_tickets.html",{"server":server.values()})
    return HttpResponseRedirect("/")

def tickets(request,t_type):
    type_form = {
                 "server": ServerForm,
                 "upgrade": UpgradeForm,
                 "virtual": VirtualForm,
                 "update": UpdateForm,
                 "fix": FixForm,
                }
    try:
        t_type = str(t_type)
    except ValueError:
        raise Http404()
    if request.session.get("status",False) and request.method == "POST":
        form = type_form[t_type](request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            print cd["over_user"]
            make_user = form.save(commit=False)
            make_user.make_user = request.session.get("user")
            make_user.tic_type = t_type
            make_user.tic_id = makemd5(str(now()) + str(make_user.make_user))
            make_user.save()
            for i in cd["over_user"]:
                over = UserAuth.objects.get(user=str(i))
                a = make_user.over_user.add(over)
            make_user.save()
            #over = UserAuth.objects.get(user="kundong@gridinfo.com.cn")
            #a = make_user.over_user.add(over)
            #make_user.save()
            return HttpResponseRedirect("/my_tickets/")
    if request.session.get("status",False) and request.method == "GET":
        form = type_form[t_type]()
    return render_to_response("send_tickets.html",{"form":form,"t_type":t_type},\
                              context_instance=RequestContext(request))

def reply(request,tic_id):
    try:
        tic_id = str(tic_id)
        form_msg = AllForm.objects.get(tic_id=tic_id)
    except ValueError:
        raise Http404()
    reply_msg = []
    r_msg = []
    behind = []
    if int(form_msg.reply) != 0:
        reply_msg = FormMsg.objects.filter(tic_id=tic_id).values()
        for i in reply_msg:
            formmsg_get = FormMsg.objects.get(formid=i["formid"])
            come_from = formmsg_get.user.user
            for n in formmsg_get.behind.values():
                behind.append(n["user"])
            a = [i["msg"],i["formid"],come_from,behind]
            behind = []
            r_msg.append(a)
    print r_msg
    if request.session.get("status",False) and request.method == "POST":
        form = ReplyForm(request.POST)
        user = request.session.get("user")
        if form.is_valid():
            cd = form.cleaned_data
            reply = form.save(commit=False)
            reply.tic_id = tic_id
            reply.queue = str(int(form_msg.reply) + 1)
            AllForm.objects.filter(tic_id=tic_id).update(reply=reply.queue)
            reply.user = UserAuth.objects.get(user=str(user))
            reply.save()
            for i in cd["behind"]:
                behind_user = UserAuth.objects.get(user=str(i))
                behind = reply.behind.add(behind_user)
            reply.save()
            return HttpResponseRedirect("/my_tickets/")
    if request.session.get("status",False) and request.method == "GET":
        form = ReplyForm()
    return render_to_response("reply.html",{"form_msg":form_msg,"reply_msg":r_msg,\
                                    "form":form},context_instance=RequestContext(request))
