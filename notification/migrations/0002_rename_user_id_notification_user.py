# Generated by Django 4.0.5 on 2022-06-14 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='user_id',
            new_name='user',
        ),
    ]