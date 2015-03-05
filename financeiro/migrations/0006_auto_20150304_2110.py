# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0005_auto_20150304_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 5, 0, 10, 20, 867240, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 5, 0, 10, 20, 867240, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='status_peca',
            field=models.CharField(blank=True, verbose_name='status peça', null=True, max_length=1, choices=[('0', 'aguardando cliente'), ('1', 'em trânsito'), ('2', 'entregue')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='status_venda',
            field=models.CharField(blank=True, default=0, null=True, max_length=1, choices=[('0', 'aberta'), ('1', 'encerrada')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 5, 0, 10, 20, 867240, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
