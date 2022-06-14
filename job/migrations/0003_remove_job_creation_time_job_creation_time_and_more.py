# Generated by Django 4.0.5 on 2022-06-14 19:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_creation_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Creation_time',
        ),
        migrations.AddField(
            model_name='job',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 6, 14, 19, 4, 12, 962245, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
