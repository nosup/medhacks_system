# Generated by Django 2.0.4 on 2018-04-16 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='post',
        ),
    ]