# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20150226_1019'),
        ('financeiro', '0004_auto_20150226_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDeVenda',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('quantidade', models.PositiveSmallIntegerField(default=1)),
                ('valor_venda', models.DecimalField(decimal_places=2, blank=True, verbose_name='valor venda', max_digits=5, null=True)),
                ('peca', models.ManyToManyField(to='catalogo.Peca', verbose_name='peça')),
                ('venda', models.ForeignKey(to='financeiro.Venda')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parcela',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número da parcela', default=0)),
                ('data', models.DateField(default=datetime.datetime(2015, 2, 26, 13, 19, 5, 330946, tzinfo=utc))),
                ('valor', models.DecimalField(validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], decimal_places=2, default=Decimal('0.00'), max_digits=5)),
                ('venda', models.ForeignKey(to='financeiro.Venda')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('tipo', models.PositiveSmallIntegerField(default=1, choices=[('1', 'Romaneio'), ('2', 'Nota Fiscal')])),
                ('numero', models.PositiveSmallIntegerField(blank=True, verbose_name='número', null=True)),
                ('data', models.DateField(default=datetime.datetime(2015, 2, 26, 13, 19, 5, 330946, tzinfo=utc))),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
                ('loja', models.ForeignKey(to='financeiro.Loja')),
                ('viagem', models.ForeignKey(to='financeiro.Viagem')),
            ],
            options={
                'ordering': ('data', 'pub_date'),
                'verbose_name_plural': 'Notas Fiscais',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='notafiscal',
            name='loja',
        ),
        migrations.RemoveField(
            model_name='notafiscal',
            name='viagem',
        ),
        migrations.DeleteModel(
            name='NotaFiscal',
        ),
        migrations.AlterModelOptions(
            name='cidade',
            options={'ordering': ('cidade', 'pub_date')},
        ),
        migrations.AlterModelOptions(
            name='venda',
            options={'ordering': ('data', 'pub_date')},
        ),
        migrations.AlterModelOptions(
            name='viagem',
            options={'ordering': ('data', 'pub_date'), 'verbose_name_plural': 'viagens'},
        ),
        migrations.RemoveField(
            model_name='venda',
            name='data_da_venda',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='numero_da_venda',
        ),
        migrations.RemoveField(
            model_name='viagem',
            name='data_da_viagem',
        ),
        migrations.AddField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 13, 19, 5, 330946, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 13, 19, 5, 330946, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guia',
            name='nota',
            field=models.CharField(max_length=1, default=3, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loja',
            name='nota',
            field=models.CharField(max_length=1, default=3, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='marca',
            name='nota',
            field=models.CharField(max_length=1, default=3, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopping',
            name='nota',
            field=models.CharField(max_length=1, default=3, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='forma_de_pagamento',
            field=models.CharField(max_length=3, default='DIN', choices=[('DIN', 'dinheiro'), ('CAD', 'caderninho'), ('CAR', 'cartão'), ('PGS', 'PagSeguro')]),
            preserve_default=True,
        ),
    ]
