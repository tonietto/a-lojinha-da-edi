# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_auto_20150304_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='data_de_fechamento',
            field=models.DateTimeField(null=True, blank=True, verbose_name='fechamento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='venda',
            name='status_peca',
            field=models.PositiveSmallIntegerField(default=0, choices=[('0', 'aberta'), ('1', 'encerrada')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='venda',
            name='status_venda',
            field=models.PositiveSmallIntegerField(default=0, choices=[('0', 'aberta'), ('1', 'encerrada')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 23, 53, 5, 431647, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 23, 53, 5, 431647, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='abertura'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 23, 53, 5, 431647, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
