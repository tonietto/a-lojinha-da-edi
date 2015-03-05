# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0007_auto_20150304_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='data_de_fechamento',
            field=models.DateTimeField(null=True, verbose_name='fechamento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 5, 0, 30, 2, 767655, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 5, 0, 30, 2, 767655, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 5, 0, 30, 2, 767655, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
