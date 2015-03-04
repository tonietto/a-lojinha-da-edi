# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0012_auto_20150303_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidade',
            options={'ordering': ('data_de_edicao', 'cidade')},
        ),
        migrations.AlterModelOptions(
            name='guia',
            options={'ordering': ('data_de_edicao', 'nome')},
        ),
        migrations.AlterModelOptions(
            name='loja',
            options={'ordering': ('data_de_edicao', 'nome')},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'ordering': ('data_de_edicao', 'nome')},
        ),
        migrations.AlterModelOptions(
            name='parcela',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='peca',
            options={'verbose_name': 'peça', 'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='recibo',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='shopping',
            options={'ordering': ('data_de_edicao', 'nome')},
        ),
        migrations.AlterModelOptions(
            name='venda',
            options={'ordering': ('data', 'data_de_edicao')},
        ),
        migrations.AlterModelOptions(
            name='viagem',
            options={'verbose_name_plural': 'viagens', 'ordering': ('data_de_edicao', 'data')},
        ),
        migrations.RemoveField(
            model_name='cidade',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='guia',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='loja',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='viagem',
            name='custo_total',
        ),
        migrations.RemoveField(
            model_name='viagem',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='cidade',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 25, 55028, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidade',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 26, 56055, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guia',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 27, 845028, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guia',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 29, 116084, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loja',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 30, 95311, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loja',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 31, 62129, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marca',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 32, 19149, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marca',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 32, 930099, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parcela',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 33, 875008, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parcela',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 35, 45123, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peca',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 36, 125141, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peca',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 37, 160153, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recibo',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 38, 172141, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recibo',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 39, 162263, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopping',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 40, 130198, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopping',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 41, 109163, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venda',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 42, 110212, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venda',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 43, 21031, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viagem',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 43, 977238, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viagem',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 44, 900221, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 12, 58, 55, 113130, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 12, 58, 55, 113130, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 3, 4, 12, 58, 55, 113130, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
