# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='creation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payement_date',
            field=models.DateField(),
        ),
    ]
