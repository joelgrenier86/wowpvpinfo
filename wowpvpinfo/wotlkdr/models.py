from django.db import models

# Create your models here.
class Skill(models.Model):
    skill_name = models.CharField(max_length=25)
    class_name = models.CharField(max_length=15)
    dr_cat = models.CharField(max_length = 20)