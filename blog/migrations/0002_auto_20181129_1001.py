# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-29 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
