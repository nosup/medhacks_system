# Generated by Django 2.0.4 on 2018-04-27 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20180426_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='attended',
            field=models.CharField(default='No', max_length=50),
        ),
    ]