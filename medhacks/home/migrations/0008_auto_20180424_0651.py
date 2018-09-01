# Generated by Django 2.0.4 on 2018-04-24 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180424_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='address1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='address2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='graduating_class',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='major',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='reimbursement',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='university',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='application',
            name='zipcode',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
