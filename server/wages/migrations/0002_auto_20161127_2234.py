# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wage',
            name='first_name',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='wage',
            name='last_name',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='wage',
            name='wage',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wage',
            name='year',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
