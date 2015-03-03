# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_auto_20150302_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagsdapeca',
            options={'ordering': ('pub_date', 'tag')},
        ),
        migrations.AlterField(
            model_name='peca',
            name='custo_unitario',
            field=models.DecimalField(verbose_name='custo R$', decimal_places=2, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='peca',
            name='preco_unitario',
            field=models.DecimalField(verbose_name='preço R$', decimal_places=2, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='peca',
            name='preco_unitario_promocional',
            field=models.DecimalField(blank=True, max_digits=5, default=Decimal('0.00'), null=True, verbose_name='preço promocional R$', decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='peca',
            name='tags',
            field=models.ManyToManyField(blank=True, to='catalogo.TagsDaPeca'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quantidadedepecasportamanho',
            name='quantidade_comprada',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quantidadedepecasportamanho',
            name='quantidade_em_estoque',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
