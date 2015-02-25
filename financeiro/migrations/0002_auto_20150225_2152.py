# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viagem',
            options={'verbose_name_plural': 'viagens', 'ordering': ('data_da_viagem', 'pub_date')},
        ),
        migrations.RemoveField(
            model_name='viagem',
            name='data',
        ),
        migrations.AddField(
            model_name='viagem',
            name='data_da_viagem',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 25, 21, 52, 30, 124551, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
