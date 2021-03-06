# Generated by Django 2.0.4 on 2018-07-23 23:37

from django.db import migrations, models
import travel.formatcheck


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_trapplication_type_reim'),
    ]

    operations = [
        migrations.AddField(
            model_name='trapplication',
            name='first_name',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='last_name',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='permanent_address1',
            field=models.CharField(blank=True, default='-', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='permanent_address2',
            field=models.CharField(blank=True, default='-', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='permanent_city',
            field=models.CharField(blank=True, default='-', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='permanent_state',
            field=models.CharField(blank=True, default='-', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='permanent_zip',
            field=models.CharField(blank=True, default='-', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='policy_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='receipt_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='receipt_file',
            field=travel.formatcheck.ContentTypeRestrictedFileField(default='-', upload_to='receipts'),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='reimburse_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='travel_date_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='travel_date_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='travel_location_city',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='trapplication',
            name='travel_location_state',
            field=models.CharField(default='NA', max_length=50),
        ),
    ]
