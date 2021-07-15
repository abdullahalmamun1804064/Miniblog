from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import Addpost, u_signup,u_loging
from .models import post

# Home page
def home (request):
    Post=post.objects.all()
    dic={
        'posts':Post,
    }
    return render(request,'blog/home.html',dic)

# About page
def about(request):
    return render(request,'blog/about.html')

# Contract page
def contract(request):
    return render(request,'blog/contact.html')

# Deshboard
def deshboard(request):
    if request.user.is_authenticated:
        Post=post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        dic={
        'posts': Post,
        'full_name':full_name,
        'user':user,
        'group':gps,
        }
        return render(request,'blog/deshboard.html',dic)
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Signup
def user_signup(request):
    if request.method=="POST":
        fm=u_signup(request.POST)
        if fm.is_valid():
            user=fm.save()
            messages.success(request,'Congertulations !!! You have become an Author !!!')
            group=Group.objects.get(name='Author')
            user.groups.add(group)

    else:
        fm=u_signup()
    dic ={
        'form':fm,
    }
    return render(request,'blog/signup.html',dic)

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=u_loging(request=request,data=request.POST)
            if fm.is_valid():
                un=fm.cleaned_data['username']
                up=fm.cleaned_data['password']
                user=authenticate(username=un,password=up)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Loging successful !!!!')
                    return HttpResponseRedirect('/deshboard/')
        else:
            fm=u_loging()
        dic ={
            'form':fm,
        }
        
        return render(request,'blog/login.html',dic)
    else:
         return HttpResponseRedirect('/deshboard/')

# AddPost
def addpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=Addpost(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Post Create Successfully !!!')
                fm=Addpost()
        else:
           fm=Addpost()
        dic={
             'form':fm,
            }
        return render(request,'blog/addpost.html',dic)
    else:
        return HttpResponseRedirect('/login/')

# UpdatePost
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi=post.objects.get(pk=id)
            fm=Addpost(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Post Update Successfully !!!')
                return HttpResponseRedirect('/deshboard/')
        else:
           pi=post.objects.get(pk=id)
           fm=Addpost(instance=pi)
        dic={
             'form':fm,
            }
        return render(request,'blog/updatepost.html',dic)
    else:
        return HttpResponseRedirect('/login/')

# DeletePost
def deletepost(request,id):
    if request.user.is_authenticated:
        pi=post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/deshboard/')
    else:
        return HttpResponseRedirect('/login/')