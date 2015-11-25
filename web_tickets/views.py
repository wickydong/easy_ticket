#! /usr/bin/python
# -*- coding: utf-8 -*-
# __author__: wickydong

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from web_tickets.models import *
from web_tickets.forms import *
import md5,datetime
import mail

def makemd5(msg):
    make = md5.new()
    make.update(msg)
    return make.hexdigest()
def now():
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return now

def index(request):
    if request.session.get("status",False):   #用户已登录则跳转,上线需开启
        return HttpResponseRedirect("/my_tickets/")
    return render_to_response("index.html") 

def logout(request):
    if request.session.get("user"):
        del request.session["user"]
        del request.session["status"]
    return HttpResponseRedirect("/login_form/")

def login_form(request):
    tic_id = request.GET.get("tic_id","")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user_msg = UserAuth.objects.get(user=cd["user"])
                if str(user_msg.passwd) == cd["passwd"]:
                    request.session["user"] = cd["user"]
                    request.session["status"] = True
                    if tic_id:
                        return HttpResponseRedirect("/reply/%s/" %tic_id)
                    return HttpResponseRedirect("/my_tickets/")
            except UserAuth.DoesNotExist:
                print "Message Is DoesNotExist"
    else:
        if request.session.get("status",False):   #用户已登录则跳转,上线需开启
            return HttpResponseRedirect("/my_tickets/")
        form = LoginForm()
    return render_to_response("login.html",{"form": form,"tic_id" :tic_id},\
                  context_instance=RequestContext(request))
    

def my_tickets(request):
    if request.session.get("status",False):
        user = request.session.get("user")
        if request.method == "POST":      #GET请求展示工单,POST请求处理工单
            return HttpResponseRedirect("/")
        else:
            server = AllForm.objects.filter(make_user=user)
            overmsg = UserAuth.objects.get(user=user)
            overmsg = overmsg.allform_set.values()
            return render_to_response("my_tickets.html",{"server":server.values(),"overmsg":overmsg})
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
    if not request.session.get("status"):
        return HttpResponseRedirect("/")
    if request.session.get("status",False) and request.method == "POST":
        form = type_form[t_type](request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            make_user = form.save(commit=False)
            make_user.make_user = request.session.get("user")
            make_user.tic_type = t_type
            make_user.tic_id = makemd5(str(now()) + str(make_user.make_user))
            make_user.save()
            over_user_list = []
            for i in cd["over_user"]:
                over_user_list.append(str(i))
                over = UserAuth.objects.get(user=str(i))
                a = make_user.over_user.add(over)
            make_user.save()
            sub = "From " + str(request.session.get("user")) + " To U's Tickets"
            url = str(make_user.tic_id)
            content = "相关信息请点击链接查看并回复: http://yoogane.sunzhongwei.com:8787/reply/%s/ \n\n\n本邮件由系统发出，请勿直接回复本邮件。" %url
            send = mail.send_mail(sub,content,over_user_list)
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
    if not request.session.get("status"):
        return HttpResponseRedirect("/login_form/?tic_id=%s"%tic_id)
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
            behind_list = []
            for i in cd["behind"]:
                behind_list.append(str(i))
                behind_user = UserAuth.objects.get(user=str(i))
                behind = reply.behind.add(behind_user)
            reply.save()
            sub = "From " + str(request.session.get("user")) + " Reply To U's Tickets"
            content = "相关信息请点击链接查看并回复: http://yoogane.sunzhongwei.com:8787/reply/%s/ \n\n\n该邮件由系统发出，请勿直接回复本邮件。" %tic_id 
            send = mail.send_mail(sub,content,behind_list)
            return HttpResponseRedirect("/my_tickets/")
    if request.session.get("status",False) and request.method == "GET":
        print request.session.get("user")
        form = ReplyForm()
    return render_to_response("reply.html",{"form_msg":form_msg,"reply_msg":r_msg,\
                                    "form":form},context_instance=RequestContext(request))
