# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_peca_recibo'),
        ('financeiro', '0009_auto_20150226_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quantidade', models.PositiveSmallIntegerField(default=1)),
                ('valor_venda', models.DecimalField(max_digits=5, decimal_places=2, verbose_name='valor venda', null=True, blank=True)),
                ('peca', models.ManyToManyField(verbose_name='peça', to='catalogo.Peca')),
                ('venda', models.ForeignKey(to='financeiro.Venda')),
            ],
            options={
                'verbose_name': 'peça',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='itemdavenda',
            name='peca',
        ),
        migrations.RemoveField(
            model_name='itemdavenda',
            name='venda',
        ),
        migrations.DeleteModel(
            name='ItemDaVenda',
        ),
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 14, 3, 39, 960480, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recibo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 14, 3, 39, 960480, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 14, 3, 39, 960480, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 14, 3, 39, 960480, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
