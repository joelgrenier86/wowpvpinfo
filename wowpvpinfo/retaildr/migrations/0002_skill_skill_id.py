# Generated by Django 4.1.2 on 2022-11-07 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retaildr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_id',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
