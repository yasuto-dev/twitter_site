# Generated by Django 3.0.4 on 2021-11-28 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211126_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='create_time',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時'),
        ),
    ]
