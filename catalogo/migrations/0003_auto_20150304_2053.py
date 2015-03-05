# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20150304_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagsdapeca',
            options={'verbose_name_plural': 'tags das peças', 'ordering': ('data_de_edicao',)},
        ),
    ]
