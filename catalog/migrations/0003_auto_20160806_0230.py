# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-06 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20160806_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
