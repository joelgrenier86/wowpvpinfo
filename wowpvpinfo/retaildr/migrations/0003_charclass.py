# Generated by Django 4.1.2 on 2022-11-02 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retaildr', '0002_auto_20221102_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=15)),
            ],
        ),
    ]
