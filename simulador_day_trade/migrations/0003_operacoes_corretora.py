# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-28 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulador_day_trade', '0002_auto_20191128_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacoes',
            name='corretora',
            field=models.CharField(choices=[('CLEAR', 'CLEAR'), ('MODAL', 'MODAL'), ('XP', 'XP')], default='CLEAR', max_length=30, verbose_name='Corretora'),
        ),
    ]
