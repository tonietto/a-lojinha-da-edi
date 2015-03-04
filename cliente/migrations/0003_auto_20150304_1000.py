# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_cidade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ('data_de_edicao', 'nome')},
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 23, 75073, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 24, 75681, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
