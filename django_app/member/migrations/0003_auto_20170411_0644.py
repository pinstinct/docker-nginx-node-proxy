# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_celerytest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celerytest',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
