from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
import smtplib

# Create your views here.

def index(request):
    id=request.session['adminid']
    return render(request,"adminapp/index.html",{})

def view_users(request):
    data=tbl_reg.objects.all()
    return render(request,"adminapp/view_users.html",{'data':data})

def approve(request,id):
    value=tbl_reg.objects.get(id=id)
    if value.approve=="APPROVE":
        password = User.objects.make_random_password(length=6, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889") 
        new=tbl_log.objects.create(username=value.email,password=password,usertype=value.usertype)
        pas1=password
        value.password=pas1
        mail=smtplib.SMTP('smtp.mailgun.org',587)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        message= "Hello, Your username is " + new.username + " and password is " + new.password + ". Thank you."
        email=value.email
        mail.sendmail(settings.EMAIL_HOST_USER,email,message)
        value.approve="APPROVED!!!"
        value.save()
    return HttpResponseRedirect(reverse('view_users'))

def view_ausers(request):
    item=tbl_log.objects.all()
    return render(request,"adminapp/view_ausers.html",{'item':item})

def delete(request,id):
    dele=tbl_log.objects.filter(id=id).delete()
    data=tbl_log.objects.all()
    return HttpResponseRedirect(reverse('view_ausers'))

def view_search(request):
    item=tbl_csv.objects.all()
    return render(request,"adminapp/view_search.html",{'item':item})

def view_contact(request):
    this=tbl_contact.objects.all()
    return render(request,"adminapp/view_contact.html",{'this':this})

def replay(request,id):
    re=tbl_contact.objects.get(id=id)
    if request.method=="POST":
        if re.reply=="REPLY":
            msg=request.POST.get('r1')
            mail=smtplib.SMTP('smtp.mailgun.org',587)
            mail.ehlo()
            mail.starttls()
            mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
            name=re.name
            reply_mail=re.email
            reply_msg='Hi '+ name +' ,\n \t This is the reply from CCAnalyser.\n  '+ msg +'\n\t\t Thank you, \n\t\t CCAnalyser'
            mail.sendmail(settings.EMAIL_HOST_USER,reply_mail,reply_msg)
            re.reply="REPLIED!!!"
            re.save()
        return HttpResponseRedirect(reverse('view_contact'))
    return render(request,"adminapp/replay.html",{'re':re})
