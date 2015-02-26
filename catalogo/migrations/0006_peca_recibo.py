# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0006_auto_20150226_1019'),
        ('catalogo', '0005_remove_peca_recibo'),
    ]

    operations = [
        migrations.AddField(
            model_name='peca',
            name='recibo',
            field=models.ForeignKey(null=True, to='financeiro.Recibo', blank=True),
            preserve_default=True,
        ),
    ]
