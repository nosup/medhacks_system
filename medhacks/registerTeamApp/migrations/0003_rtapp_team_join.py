# Generated by Django 2.0.4 on 2018-09-04 21:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registerTeamApp', '0002_auto_20180904_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='rtapp',
            name='team_join',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
