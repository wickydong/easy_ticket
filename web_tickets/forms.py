# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    user = forms.EmailField(max_length=30,error_messages={"required":"用户名不能为空"})
    passwd = forms.CharField(max_length=30,min_length=5,\
            widget=forms.PasswordInput,error_messages={"required":"密码不能为空"})
class ServerForm(forms.Form):
    server_ip = forms.CharField(max_length=30,label="服务器IP:")
    needtime = forms.CharField(max_length=30,label="需要时长:")
    needother = forms.CharField(label="申请用途:",widget=forms.Textarea)
class UpgradeForm(forms.Form):
    upgrade = forms.CharField(max_length=100,label="升级项目:")
    howtime = forms.CharField(max_length=30,label="升级时间:")
    up_msg = forms.CharField(label="升级内容:",widget=forms.Textarea)
    up_error = forms.CharField(label="影响\措施:",widget=forms.Textarea)
class VirtualForm(forms.Form):
    virtual = forms.CharField(max_length=30,label="用途:")
    system = forms.CharField(max_length=30,label="系统:")
    needconf = forms.CharField(max_length=30,label="硬件配置:",widget=forms.Textarea)
class FixForm(forms.Form):
    fix = forms.CharField(max_length=30,label="BUG类型:")
    howtime = forms.CharField(max_length=30,label="修复时间:")
    fix_msg = forms.CharField(label="修复内容:",widget=forms.Textarea)
class UpdateForm(forms.Form):
    update = forms.CharField(max_length=30,label="更新的项目:")
    howtime = forms.CharField(max_length=30,label="更新时间:")
    update_msg = forms.CharField(label="更新内容梗概:",widget=forms.Textarea)
