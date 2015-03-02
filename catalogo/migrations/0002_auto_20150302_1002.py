# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
        ('catalogo', '0001_initial'),
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
            field=models.ForeignKey(blank=True, to='financeiro.Recibo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='peca',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='nome', to='catalogo.TagsDaPeca'),
            preserve_default=True,
        ),
    ]
