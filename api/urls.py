from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path("login/",views.Redify.as_view()),
    path("yahoo/",views.Getlog.as_view()),
    
    
]
