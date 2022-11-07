from rest_framework import serializers

from .models import Skill, CharClass
#serialize SKill model for api
class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ('skill_id', 'skill_name', 'class_name', 'dr_cat')

#and class model
class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharClass
        fields = ('class_name', 'pk')