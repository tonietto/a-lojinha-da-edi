# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0013_auto_20150304_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidade',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='guia',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='loja',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='shopping',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='venda',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='viagem',
            options={'ordering': ('data_de_edicao',), 'verbose_name_plural': 'viagens'},
        ),
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 18, 1, 49, 77649, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 18, 1, 49, 77649, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 18, 1, 49, 77649, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
