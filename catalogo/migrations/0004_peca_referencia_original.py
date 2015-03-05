# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20150304_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='peca',
            name='referencia_original',
            field=models.CharField(verbose_name='referência original', null=True, blank=True, max_length=30),
            preserve_default=True,
        ),
    ]
