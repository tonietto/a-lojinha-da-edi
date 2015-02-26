# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_peca_recibo'),
        ('financeiro', '0008_auto_20150226_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDaVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('quantidade', models.PositiveSmallIntegerField(default=1)),
                ('valor_venda', models.DecimalField(blank=True, decimal_places=2, verbose_name='valor venda', max_digits=5, null=True)),
                ('peca', models.ManyToManyField(verbose_name='peça', to='catalogo.Peca')),
                ('venda', models.ForeignKey(to='financeiro.Venda')),
            ],
            options={
                'verbose_name_plural': 'items da venda',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='itemdevenda',
            name='peca',
        ),
        migrations.RemoveField(
            model_name='itemdevenda',
            name='venda',
        ),
        migrations.DeleteModel(
            name='ItemDeVenda',
        ),
        migrations.AlterModelOptions(
            name='recibo',
            options={'ordering': ('data', 'pub_date')},
        ),
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 14, 0, 53, 492629, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recibo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 14, 0, 53, 492629, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 14, 0, 53, 492629, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 14, 0, 53, 492629, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
