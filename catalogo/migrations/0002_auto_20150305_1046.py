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
            field=models.ForeignKey(to='financeiro.Recibo', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='peca',
            name='tags',
            field=models.ManyToManyField(blank=True, to='catalogo.TagsDaPeca'),
            preserve_default=True,
        ),
    ]
