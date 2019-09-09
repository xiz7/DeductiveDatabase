"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.views import dota,deduce,pick,redo,nextS,team,enemy

urlpatterns = [

    url('dota', dota,name='dota'),
    url('^deduce/$', deduce, name='deduce'),
    url('^pick/$', pick,  name='pick'),
    url('^redo/$', redo, name='redo'),
    url('^next/$', nextS, name='next'),
    url('^team/$', team, name='team'),
    url('^enemy/$', enemy, name='enemy'),



]
