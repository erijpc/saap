# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-24 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0028_auto_20180924_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processo',
            old_name='link_camara',
            new_name='link_cam',
        ),
    ]
