# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_cliente_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(null=True, max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
