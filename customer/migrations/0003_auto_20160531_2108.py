# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 21:08
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_address_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='fax',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='tel',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='mobile',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='web',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]