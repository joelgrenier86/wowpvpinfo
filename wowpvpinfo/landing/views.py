from django.shortcuts import render
from django.urls import reverse                     
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    return render(request, 'index.html')