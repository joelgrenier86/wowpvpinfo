from django.shortcuts import render
from django.urls import reverse                     
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Skill

def index(request):
    skills = Skill.objects.all().values()
    cs = Skill.objects.filter(dr_cat__iexact = "cs")
    silence = Skill.objects.filter(dr_cat__iexact = "silence")
    cr = Skill.objects.filter(dr_cat__iexact = "CR") 
    fear = Skill.objects.filter(dr_cat__iexact = "Fear") 
    rr = Skill.objects.filter(dr_cat__iexact = "rr") 
    os = Skill.objects.filter(dr_cat__iexact = "Opener stun") 
    disorient = Skill.objects.filter(dr_cat__iexact = "Disorient") 
    incap = Skill.objects.filter(dr_cat__iexact = "incap") 
    disarm = Skill.objects.filter(dr_cat__iexact = "disarm") 
    rs = Skill.objects.filter(dr_cat__iexact = "rs") 
    horror = Skill.objects.filter(dr_cat__iexact = "horror") 
    none = Skill.objects.filter(dr_cat__iexact = "none")
    cats = Skill.objects.order_by().values_list('dr_cat').distinct()



    template = loader.get_template('wotlkdr/index.html')
    context = {
        'skills' : skills,
        'cs' : cs,
        'silence' : silence,
        'cr' : cr,
        'fear' : fear,
        'rr' : rr,
        'os' : os,
        'disorient' : disorient,
        'incap' : incap,
        'disarm' : disarm,
        'rs' : rs,
        'horror' : horror,
        'cats' : cats,
        'none' : none,
    }
    return HttpResponse(template.render(context, request ))

def lookup(request):
    skills = Skill.objects.all().values()
    clist = []
  

    class_list = Skill.objects.order_by().values('class_name').distinct()


    template = loader.get_template('wotlkdr/lookup.html')
    context = {
        'skills' : skills,
        'class_list' :class_list,
    }
    return HttpResponse(template.render(context, request ))