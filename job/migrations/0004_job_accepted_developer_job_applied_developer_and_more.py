# Generated by Django 4.0.5 on 2022-06-14 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0003_remove_job_creation_time_job_creation_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='accepted_developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepted_developer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='applied_developer',
            field=models.ManyToManyField(related_name='applied_developer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='banner_image',
            field=models.ImageField(default='cat.img', upload_to='job'),
        ),
    ]
