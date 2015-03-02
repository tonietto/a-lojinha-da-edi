# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20150302_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peca',
            name='codigo',
            field=models.CharField(blank=True, verbose_name='código', null=True, max_length=12),
            preserve_default=True,
        ),
    ]
