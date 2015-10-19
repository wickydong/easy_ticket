from django import forms


class LoginForm(forms.Form):
    user = forms.EmailField(max_length=30)
    passwd = forms.CharField(max_length=30,min_length=5)
