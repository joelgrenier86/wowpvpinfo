# Generated by Django 4.1.2 on 2022-11-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=25)),
                ('class_name', models.CharField(max_length=15)),
                ('dr_cat', models.CharField(max_length=20)),
            ],
        ),
    ]
