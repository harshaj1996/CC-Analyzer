from django.db import models

#username-fraudcard password-card

# Create your models here.

class tbl_log(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)

class tbl_reg(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    purpose=models.CharField(max_length=1000)
    approve=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class tbl_csv(models.Model):
    name=models.CharField(max_length=50)
    loc=models.FileField(upload_to='media',verbose_name="file",null=True,blank=True)
    total=models.CharField(max_length=50)
    sample=models.CharField(max_length=50)
    true=models.CharField(max_length=50)
    false=models.CharField(max_length=50)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)

class tbl_contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=1000)
    message=models.CharField(max_length=10000)
    reply=models.CharField(max_length=50)

