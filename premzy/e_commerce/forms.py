from django import forms

from .models import Register


class register(forms.Form):
	first_name   = forms.CharField(max_length=150)
	middle_name  = forms.CharField(max_length=150)
	last_name    = forms.CharField(max_length=150)
	email        = forms.EmailField(max_length=150)
	username     = forms.CharField(max_length=150)
	password     = forms.CharField(max_length=50)
	password1    = forms.CharField(max_length=50)


