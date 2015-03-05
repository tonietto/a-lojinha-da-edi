# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150304_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 4, 23, 53, 5, 419635, tzinfo=utc), verbose_name='editado em'),
            preserve_default=True,
        ),
    ]
