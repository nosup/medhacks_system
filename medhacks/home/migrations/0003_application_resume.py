# Generated by Django 2.0.4 on 2018-04-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_application_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.FileField(default='nothing', upload_to='Resume'),
        ),
    ]