# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20150226_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='peca',
            name='codigo',
            field=models.PositiveSmallIntegerField(verbose_name='código', null=True),
            preserve_default=True,
        ),
    ]
