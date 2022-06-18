# Generated by Django 4.0.5 on 2022-06-18 01:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Creation_time',
        ),
        migrations.RemoveField(
            model_name='job',
            name='Modification_time',
        ),
        migrations.AddField(
            model_name='job',
            name='accepted_developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepted_developer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='applied_developer',
            field=models.ManyToManyField(blank=True, null=True, related_name='applied_developer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='banner_image',
            field=models.ImageField(default='job.jpg', upload_to='media'),
        ),
        migrations.AddField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 6, 18, 1, 21, 10, 219924, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
