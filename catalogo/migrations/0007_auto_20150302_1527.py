# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20150302_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peca',
            name='codigo',
        ),
        migrations.AlterField(
            model_name='peca',
            name='nome',
            field=models.CharField(default='', max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='peca',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]
