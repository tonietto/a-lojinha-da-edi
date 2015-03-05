# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0004_auto_20150304_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 5, 0, 6, 25, 560578, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 5, 0, 6, 25, 560578, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='forma_caderninho',
            field=models.CharField(max_length=3, verbose_name='forma de pagamento no caderninho', blank=True, choices=[('DIN', 'dinheiro'), ('PAR', 'parcelado'), ('DEP', 'depósito')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='forma_cartao',
            field=models.CharField(max_length=1, verbose_name='forma de pagamento no cartão', blank=True, choices=[('C', 'crédito'), ('D', 'débito')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='forma_de_pagamento',
            field=models.CharField(max_length=3, choices=[('DIN', 'dinheiro'), ('CAD', 'caderninho'), ('CAR', 'cartão'), ('PGS', 'PagSeguro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='numero_de_parcelas',
            field=models.CharField(max_length=1, blank=True, choices=[('1', '1x'), ('2', '2x'), ('3', '3x'), ('4', '4x')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='status_peca',
            field=models.PositiveSmallIntegerField(null=True, blank=True, choices=[('0', 'aberta'), ('1', 'encerrada')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='status_venda',
            field=models.PositiveSmallIntegerField(null=True, blank=True, default=0, choices=[('0', 'aberta'), ('1', 'encerrada')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 5, 0, 6, 25, 560578, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
