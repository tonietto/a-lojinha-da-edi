# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.utils.timezone import utc
from decimal import Decimal
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0011_auto_20150303_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='custo_total',
            field=models.DecimalField(max_digits=5, default=Decimal('0.00'), null=True, blank=True, verbose_name='custo total', decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 3, 20, 30, 52, 987931, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 3, 20, 30, 52, 987931, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 3, 20, 30, 52, 987931, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
