# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_auto_20150225_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notafiscal',
            name='data_da_nota',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 25, 21, 56, 58, 347917, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data_da_venda',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 25, 21, 56, 58, 347917, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data_da_viagem',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 25, 21, 56, 58, 347917, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
