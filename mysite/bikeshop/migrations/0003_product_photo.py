# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeshop', '0002_auto_20160209_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.FileField(blank=True, upload_to='product_photo'),
        ),
    ]