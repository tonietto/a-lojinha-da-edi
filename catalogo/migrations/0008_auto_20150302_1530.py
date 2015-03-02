# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_auto_20150302_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peca',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tagsdapeca',
            name='slug',
        ),
    ]
