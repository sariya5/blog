# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(max_length=3),
        ),
    ]