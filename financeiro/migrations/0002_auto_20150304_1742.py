# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 20, 42, 21, 28273, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='peca',
            name='tamanhos',
            field=models.ManyToManyField(to='catalogo.TamanhoDaPeca'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 20, 42, 21, 28273, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 20, 42, 21, 28273, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
