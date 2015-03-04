# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150304_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 4, 18, 1, 49, 60488, tzinfo=utc), verbose_name='editado em'),
            preserve_default=True,
        ),
    ]
