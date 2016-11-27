# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20161107_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentedequipment',
            name='equipment_id',
            field=models.ForeignKey(blank=True, db_column='equipment_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Equipment'),
        ),
        migrations.AlterField(
            model_name='rentedequipment',
            name='request_id',
            field=models.ForeignKey(blank=True, db_column='request_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Request'),
        ),
    ]