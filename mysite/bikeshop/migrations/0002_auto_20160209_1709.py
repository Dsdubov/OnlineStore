# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bikeshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
