# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_auto_20160518_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceline',
            name='unit_price',
            field=models.FloatField(),
        ),
    ]
