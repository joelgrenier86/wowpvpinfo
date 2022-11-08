# Generated by Django 4.1.2 on 2022-11-02 21:35

from django.db import migrations
def add_retail_skills(apps, schema_editor):
    Skill = apps.get_model('retaildr', 'Skill')
    skills=[]
    textFile = open(r'C:\Users\Joel\Documents\projects\WowPvpInfo\wowpvpinfo\retaildr\static\retailDrInfo.txt', 'r')
    byLine = textFile.readlines()
    for line in byLine:
        print(line)
        data = line.split(',')
        skill =(data[0], data[1], data[2],data[3])
        skills.append(skill)
    for skill in skills:
        Skill.objects.create(skill_id = skill[0],skill_name = skill[2],dr_cat = skill[1],class_name=skill[3])

class Migration(migrations.Migration):

    dependencies = [
        ('retaildr', '0002_skill_skill_id'),
    ]

    operations = [
        migrations.RunPython(add_retail_skills)
    ]
