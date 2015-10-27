from django import forms


class LoginForm(forms.Form):
    user = forms.EmailField(max_length=30)
    passwd = forms.CharField(max_length=30,min_length=5)
class ServerForm(forms.Form):
    server = forms.EmailField(max_length=30)
    passwd = forms.CharField(max_length=30,min_length=5)
class UpgradeForm(forms.Form):
    user = forms.EmailField(max_length=30)
    passwd = forms.CharField(max_length=30,min_length=5)
class VirtualForm(forms.Form):
    user = forms.EmailField(max_length=30)
    passwd = forms.CharField(max_length=30,min_length=5)
class UpdateForm(forms.Form):
    user = forms.EmailField(max_length=30)
    passwd = forms.CharField(max_length=30,min_length=5)
class OnlineForm(forms.Form):
    user = forms.EmailField(max_length=30)
    passwd = forms.CharField(max_length=30,min_length=5)
