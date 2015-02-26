# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20150226_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peca',
            name='nota_fiscal',
        ),
        migrations.RemoveField(
            model_name='peca',
            name='valor_venda',
        ),
        migrations.RemoveField(
            model_name='peca',
            name='venda',
        ),
    ]
