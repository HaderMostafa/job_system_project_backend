# Generated by Django 4.0.5 on 2022-06-17 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_merge_20220617_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='banner_image',
            field=models.ImageField(default='job.jpg', upload_to='media'),
        ),
    ]
