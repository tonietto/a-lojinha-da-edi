# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_peca_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peca',
            name='codigo',
            field=models.PositiveSmallIntegerField(db_column='codigo_automatico', null=True, verbose_name='código'),
            preserve_default=True,
        ),
    ]
