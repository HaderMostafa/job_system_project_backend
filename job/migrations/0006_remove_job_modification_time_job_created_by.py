# Generated by Django 4.0.4 on 2022-06-16 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import job.validator


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0005_alter_job_applied_developer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Modification_time',
        ),
        migrations.AddField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL, validators=[job.validator.validate_file_extension]),
        ),
    ]
