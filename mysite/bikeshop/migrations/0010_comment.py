# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bikeshop', '0009_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='bikeshop.Product')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to='bikeshop.UserProfile')),
            ],
        ),
    ]