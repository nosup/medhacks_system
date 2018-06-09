# Generated by Django 2.0.4 on 2018-06-06 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='travel_reimbursement',
            field=models.CharField(choices=[('-', 'Not Decided'), ('Regional', 'Regional'), ('National', 'National'), ('International', 'International')], default='-', max_length=13),
        ),
    ]
