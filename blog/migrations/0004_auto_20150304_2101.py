# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150304_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 5, 0, 1, 1, 727685, tzinfo=utc), verbose_name='editado em'),
            preserve_default=True,
        ),
    ]
