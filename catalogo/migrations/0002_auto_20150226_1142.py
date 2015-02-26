# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peca',
            name='marca',
            field=models.ForeignKey(to='financeiro.Marca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='peca',
            name='recibo',
            field=models.ForeignKey(null=True, blank=True, to='financeiro.Recibo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='peca',
            name='tags',
            field=models.ManyToManyField(related_name='nome', to='catalogo.TagsDaPeca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='peca',
            name='tamanho',
            field=models.ForeignKey(to='catalogo.TamanhoDaPeca'),
            preserve_default=True,
        ),
    ]
