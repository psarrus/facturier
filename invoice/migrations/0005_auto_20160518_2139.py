# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20160509_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceline',
            name='unit_price',
            field=models.FloatField(),
        ),
    ]
