# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-06 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_release_embed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='price',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=None, default_currency=b'USD', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='length',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
