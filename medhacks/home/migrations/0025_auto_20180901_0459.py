# Generated by Django 2.0.4 on 2018-09-01 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20180628_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='reimbursement',
            field=models.CharField(default='No', max_length=50),
        ),
    ]
