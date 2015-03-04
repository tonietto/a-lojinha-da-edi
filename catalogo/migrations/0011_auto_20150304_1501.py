# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_auto_20150304_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriadapeca',
            options={'ordering': ('data_de_edicao',), 'verbose_name': 'categoria'},
        ),
        migrations.AlterModelOptions(
            name='cordapeca',
            options={'verbose_name_plural': 'cores', 'verbose_name': 'cor', 'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='peca',
            options={'ordering': ('data_de_edicao',), 'verbose_name': 'peça'},
        ),
        migrations.AlterModelOptions(
            name='quantidadedepecasportamanho',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='tagsdapeca',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='tamanhodapeca',
            options={'ordering': ('data_de_edicao',), 'verbose_name': 'tamanho'},
        ),
        migrations.AlterField(
            model_name='peca',
            name='preco_unitario_promocional',
            field=models.DecimalField(max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], decimal_places=2, blank=True, null=True, verbose_name='promoção R$'),
            preserve_default=True,
        ),
    ]
