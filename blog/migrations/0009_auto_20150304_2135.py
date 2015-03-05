# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150304_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(verbose_name='editado em', default=datetime.datetime(2015, 3, 5, 0, 35, 12, 72545, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
