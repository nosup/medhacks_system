# Generated by Django 2.0.4 on 2018-04-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_application_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='first_name',
            field=models.CharField(default='-', max_length=50),
        ),
    ]