# Generated by Django 5.1.2 on 2024-11-15 17:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_task_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
    ]