# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20160509_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payement_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
