# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-19 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0052_merge_20180416_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingestjob',
            name='regulated_datum',
        ),
        migrations.RemoveField(
            model_name='ingestjob',
            name='transformed_datum',
        ),
    ]