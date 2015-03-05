# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cidade',
            field=models.ForeignKey(blank=True, to='financeiro.Cidade'),
            preserve_default=True,
        ),
    ]
