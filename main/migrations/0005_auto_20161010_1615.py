# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_equipmentsrented'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offices',
            new_name='Office',
        ),
        migrations.RenameModel(
            old_name='EquipmentsRented',
            new_name='RentedEquipment',
        ),
    ]
