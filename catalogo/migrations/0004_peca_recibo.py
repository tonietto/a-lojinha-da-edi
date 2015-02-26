# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20150226_1019'),
        ('financeiro', '0005_auto_20150226_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='peca',
            name='recibo',
            field=models.ForeignKey(to='financeiro.Recibo', blank=True, null=True),
            preserve_default=True,
        ),
    ]
