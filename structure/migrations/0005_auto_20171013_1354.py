# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-13 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0004_auto_20171013_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identifiedsites',
            old_name='protein',
            new_name='protein_conformation',
        ),
    ]
