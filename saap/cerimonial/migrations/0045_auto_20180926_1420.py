# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-26 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0044_auto_20180926_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='localtrabalho',
            name='numero',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Número'),
        ),
    ]