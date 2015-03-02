# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_auto_20150302_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peca',
            name='marca',
            field=models.ForeignKey(to='financeiro.Marca'),
            preserve_default=True,
        ),
    ]
