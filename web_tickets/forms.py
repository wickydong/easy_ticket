# -*- coding: utf-8 -*-
from django import forms
from web_tickets.models import *

choices = (("bingchunmu@gridinfo.com.cn","秉淳"),("kundong@gridinfo.com.cn","董琨"),\
           ("lizhiluan@gridinfo.com.cn","栾立志"),("jikunzhang@gridinfo.com.cn","张继坤")



)

class LoginForm(forms.Form):
    user = forms.EmailField(max_length=30,error_messages={"required":"用户名不能为空"})
    passwd = forms.CharField(max_length=30,min_length=5,\
            widget=forms.PasswordInput,error_messages={"required":"密码不能为空"})
class ServerForm(forms.ModelForm):
    class Meta:
        model = AllForm
        #exclude = ['make_user',]
        fields = ("name","howtime","msg","over_user")
    name = forms.CharField(max_length=30,label="服务器IP:")
    howtime = forms.CharField(max_length=30,label="需要时长:")
    msg = forms.CharField(label="申请用途:",widget=forms.Textarea)
    over_user = forms.MultipleChoiceField(label="处理人:",choices=choices,widget=forms.CheckboxSelectMultiple)
class UpgradeForm(forms.ModelForm):
    class Meta:
        model = AllForm
        fields = ("name","howtime","msg","qus","over_user")
    name = forms.CharField(max_length=100,label="升级项目:")
    howtime = forms.CharField(max_length=30,label="升级时间:")
    msg = forms.CharField(label="升级内容:",widget=forms.Textarea)
    qus = forms.CharField(label="影响\措施:",widget=forms.Textarea)
class VirtualForm(forms.ModelForm):
    class Meta:
        model = AllForm
        fields = ("name","sys","conf","over_user")
    name = forms.CharField(max_length=30,label="用途:")
    sys = forms.CharField(max_length=30,label="系统:")
    conf = forms.CharField(max_length=30,label="硬件配置:")
class FixForm(forms.ModelForm):
    class Meta:
        model = AllForm
        fields = ("name","howtime","msg","over_user")
    name = forms.CharField(max_length=30,label="BUG类型:")
    howtime = forms.CharField(max_length=30,label="修复时间:")
    msg = forms.CharField(label="修复内容:",widget=forms.Textarea)
class UpdateForm(forms.ModelForm):
    class Meta:
        model = AllForm
        fields = ("name","howtime","msg","over_user")
    name = forms.CharField(max_length=30,label="更新的项目:")
    howtime = forms.CharField(max_length=30,label="更新时间:")
    msg = forms.CharField(label="更新内容梗概:",widget=forms.Textarea)


class ReplyForm(forms.ModelForm):
    class Meta:
        model = FormMsg
        fields = ("msg","behind")
    msg = forms.CharField(label="回复内容:",widget=forms.Textarea)
    behind = forms.MultipleChoiceField(label="处理人:",choices=choices,widget=forms.CheckboxSelectMultiple)
