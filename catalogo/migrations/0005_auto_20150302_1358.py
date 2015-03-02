# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20150302_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peca',
            name='marca',
            field=models.ForeignKey(to='financeiro.Marca', blank=True),
            preserve_default=True,
        ),
    ]
