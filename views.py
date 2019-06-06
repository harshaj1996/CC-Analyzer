from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
import smtplib

# Create your views here.

def home(request):
    return render(request,"publicapp/home.html",{})

def about(request):
    return render(request,"publicapp/about.html",{})

def service(request):
    return render(request,"publicapp/service.html",{})

def terms(request):
    return render(request,"publicapp/terms.html",{})

def register(request):
    msg=""
    data=tbl_reg.objects.all()
    if request.method=="POST":
        na=request.POST.get('r1')
        mail=request.POST.get('r2')
        designation=request.POST.get('r3')
        purpose=request.POST.get('r4')
        if tbl_reg.objects.filter(email=mail):
            msg="username already taken. Please choose another.."
        else:
            data=tbl_reg.objects.create(name=na,email=mail,designation=designation,purpose=purpose,password='null',usertype='user',approve='APPROVE')
            return render(request,"publicapp/rsuccess.html",{})
    return render(request,"publicapp/register.html",{'msg':msg})

def login(request):
    if request.method=="POST":
        uname=request.POST.get('l1')
        psw=request.POST.get('l2')
        if tbl_log.objects.filter(username=uname,password=psw):
            data=tbl_log.objects.get(username=uname,password=psw)
            usertype=data.usertype
            if usertype=="admin":
                request.session["adminid"]=data.id
                return HttpResponseRedirect(reverse('index')) 
            if usertype=="user":
                data2=tbl_reg.objects.get(email=uname)
                request.session["userid"]=data2.id
                return HttpResponseRedirect(reverse('profile'))
        return render(request,"publicapp/error.html",{})
    return render(request,"publicapp/login.html",{})

def password(request):
    try:
        if request.method=="POST":
            em=request.POST.get("l1")
            new=tbl_log.objects.get(username=em)
            mail=smtplib.SMTP('smtp.mailgun.org',587)
            mail.ehlo()
            mail.starttls()
            mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
            message= "Hello, this message is from CCAnalyser-Credit Card Analysis.Your password is " + new.password + ". Thank you."
            email=new.username
            mail.sendmail(settings.EMAIL_HOST_USER,email,message)
            return render(request,"publicapp/pas.html",{})
    except:
        return render(request,"publicapp/paserror.html",{})  
    return render(request,"publicapp/password.html",{})

def paserror(request):
    return render(request,"publicapp/paserror.html",{})

def pas(request):
    return render(request,"publicapp/pas.html",{})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('home'))

def contact(request):
    if request.method=="POST":
        na=request.POST.get('c1')
        mail=request.POST.get('c2')
        sub=request.POST.get('c3')
        msg=request.POST.get('c4')
        data=tbl_contact.objects.create(name=na,email=mail,subject=sub,message=msg,reply='REPLY')
        return render(request,"publicapp/csuccess.html",{})
    return render(request,"publicapp/contact.html",{})

def rsuccess(request):
    return render(request,"publicapp/rsuccess.html",{})

def csuccess(request):
    return render(request,"publicapp/csuccess.html",{})

def error(request):
    return render(request,"publicapp/error.html",{})
