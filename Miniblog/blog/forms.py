from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.widgets import EmailInput, PasswordInput, TextInput, Textarea, Widget
from django.utils.translation import gettext,gettext_lazy as _
from .models import post

# Signup form
class u_signup(UserCreationForm):
    password1=forms.CharField(label='Password',widget=PasswordInput(attrs={'class':'form-control'})) 

    password2=forms.CharField(label='Confirm password (again)',widget=PasswordInput(attrs={'class':'form-control'})) 
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'Frist Name','last_name':'Last Name','email':'Email'}
        widgets={'username':TextInput(attrs={'class':'form-control'}),
        'first_name':TextInput(attrs={'class':'form-control'}),
        'last_name':TextInput(attrs={'class':'form-control'}),
        'email':EmailInput(attrs={'class':'form-control'}),
        }

# Loging form
class u_loging(AuthenticationForm):
    username=UsernameField(widget=TextInput(attrs={'class':'form-control','autofocus':True}))
    password=forms.CharField(label=_('Password'),strip=False,widget=PasswordInput(attrs={'class':'form-control','autocomplete':True}))

# Post form
class Addpost(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','disc']
        labels={'title':'Title Post', 'disc':'Description Post'}
        widgets={'title':TextInput(attrs={'class':'form-control'}),
        'disc':Textarea(attrs={'class':'form-control'}),
        
        }