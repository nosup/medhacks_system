# Generated by Django 2.0.4 on 2018-04-23 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_application_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='essay1',
            field=models.CharField(default='-', max_length=300),
        ),
    ]
