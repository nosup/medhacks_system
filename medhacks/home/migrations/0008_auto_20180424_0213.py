# Generated by Django 2.0.4 on 2018-04-24 02:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180423_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='essay4',
            field=models.CharField(default='-', max_length=300),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
