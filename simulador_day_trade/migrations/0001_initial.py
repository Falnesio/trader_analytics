# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-23 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data*:')),
                ('horario_de_abertura', models.TimeField(verbose_name='Hora de abertura da opera\xe7\xe3o*:')),
                ('horario_de_fechamento', models.TimeField(verbose_name='Hora de fechamento da opera\xe7\xe3o*:')),
                ('categoria', models.CharField(choices=[('FUTUROS', 'FUTUROS'), ('OPCOES', 'OP\xc7\xd5ES'), ('ACOES', 'A\xc7\xd5ES'), ('FOREX', 'FOREX')], default='FUTUROS', max_length=15)),
                ('ativo', models.CharField(default='WINFUT', max_length=30, verbose_name='Ativo*:')),
                ('sizing', models.IntegerField(default='1', verbose_name='Position size*:')),
                ('direcao', models.CharField(choices=[('C', 'Compra'), ('V', 'Venda')], max_length=30, verbose_name='Dire\xe7\xe3o*:')),
                ('estrategia', models.CharField(max_length=30, verbose_name='Estrat\xe9gia*:')),
                ('tempo_grafico_entrada', models.CharField(default='1 minuto', max_length=20, verbose_name='Tempo gr\xe1fico da entrada*:')),
                ('tempo_grafico_correlacionado', models.CharField(blank=True, max_length=20, verbose_name='Tempo gr\xe1fico correlacionado:')),
                ('risco_incial', models.DecimalField(decimal_places=2, default='-80', max_digits=15, verbose_name='Risco da Opera\xe7\xe3o*:')),
                ('resultado_operacional', models.DecimalField(decimal_places=2, default='-80', max_digits=15, verbose_name='Resultado*:')),
                ('comentarios_adicionais', models.CharField(blank=True, max_length=500, verbose_name='Coment\xe1rios adicionais:')),
            ],
            options={
                'verbose_name_plural': 'Opera\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='SimuladorDeStops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_primeiro_teste', models.DecimalField(blank=True, decimal_places=2, default='-30', max_digits=15, verbose_name='Simula\xe7\xe3o Stop Nivel 1:')),
                ('stop_segundo_teste', models.DecimalField(blank=True, decimal_places=2, default='-40', max_digits=15, verbose_name='Simula\xe7\xe3o Stop Nivel 2:')),
                ('stop_terceiro_teste', models.DecimalField(blank=True, decimal_places=2, default='-50', max_digits=15, verbose_name='Simula\xe7\xe3o Stop Nivel 3:')),
                ('stop_quarto_teste', models.DecimalField(blank=True, decimal_places=2, default='-60', max_digits=15, verbose_name='Simula\xe7\xe3o Stop Nivel 4:')),
                ('stop_quinto_teste', models.DecimalField(blank=True, decimal_places=2, default='-70', max_digits=15, verbose_name='Simula\xe7\xe3o Stop Nivel 5:')),
            ],
            options={
                'verbose_name_plural': 'Simulador de Stops',
            },
        ),
    ]
