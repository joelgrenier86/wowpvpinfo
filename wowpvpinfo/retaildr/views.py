from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters

from .serializers import SkillSerializer, ClassSerializer
from .models import Skill, CharClass


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('class_name')
    serializer_class = SkillSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['class_name', 'dr_cat']

class ClassViewSet(viewsets.ModelViewSet):
    queryset = CharClass.objects.all().order_by('class_name')
    serializer_class = ClassSerializer
    