# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_auto_20150303_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriadapeca',
            options={'verbose_name': 'categoria', 'ordering': ('data_de_edicao', 'categoria')},
        ),
        migrations.AlterModelOptions(
            name='cordapeca',
            options={'verbose_name': 'cor', 'ordering': ('data_de_edicao', 'cor'), 'verbose_name_plural': 'cores'},
        ),
        migrations.AlterModelOptions(
            name='peca',
            options={'verbose_name': 'peça', 'ordering': ('data_de_cadastro', 'nome')},
        ),
        migrations.AlterModelOptions(
            name='quantidadedepecasportamanho',
            options={'ordering': ('data_de_edicao', 'tamanho')},
        ),
        migrations.AlterModelOptions(
            name='tagsdapeca',
            options={'ordering': ('data_de_edicao', 'tag')},
        ),
        migrations.AlterModelOptions(
            name='tamanhodapeca',
            options={'verbose_name': 'tamanho', 'ordering': ('data_de_edicao', 'tamanho')},
        ),
        migrations.RemoveField(
            model_name='peca',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='tagsdapeca',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='categoriadapeca',
            name='data_de_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criação', default=datetime.datetime(2015, 3, 4, 13, 0, 7, 932868, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoriadapeca',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 9, 237883, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cordapeca',
            name='data_de_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criação', default=datetime.datetime(2015, 3, 4, 13, 0, 10, 699970, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cordapeca',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 11, 948905, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peca',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 13, 107971, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peca',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 14, 220936, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quantidadedepecasportamanho',
            name='data_de_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criação', default=datetime.datetime(2015, 3, 4, 13, 0, 16, 583998, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quantidadedepecasportamanho',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 17, 765038, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tagsdapeca',
            name='data_de_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criação', default=datetime.datetime(2015, 3, 4, 13, 0, 18, 845135, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tagsdapeca',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 19, 913972, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tamanhodapeca',
            name='data_de_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criação', default=datetime.datetime(2015, 3, 4, 13, 0, 20, 983115, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tamanhodapeca',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 22, 51024, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
