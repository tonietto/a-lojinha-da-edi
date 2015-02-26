# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peca',
            name='cor',
        ),
        migrations.AddField(
            model_name='peca',
            name='cores',
            field=models.ManyToManyField(null=True, blank=True, to='catalogo.CorDaPeca'),
            preserve_default=True,
        ),
    ]
