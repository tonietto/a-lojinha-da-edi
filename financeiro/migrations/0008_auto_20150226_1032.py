# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0007_auto_20150226_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 13, 32, 35, 380838, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recibo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 13, 32, 35, 380838, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 13, 32, 35, 380838, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 13, 32, 35, 380838, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
