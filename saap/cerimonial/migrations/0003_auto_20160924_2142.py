# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-25 00:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0002_auto_20160902_1022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['nome'], 'permissions': (('print_impressoenderecamento', 'Pode Imprimir Impressos de Endereçamento'), ('print_rel_contato_agrupado_por_processo', 'Pode Imprimir Relatório de Contatos Agrupados por Processo'), ('print_rel_contato_agrupado_por_grupo', 'Pode Imprimir Relatório de Contatos Agrupados por Grupo')), 'verbose_name': 'Contato', 'verbose_name_plural': 'Contatos'},
        ),
    ]