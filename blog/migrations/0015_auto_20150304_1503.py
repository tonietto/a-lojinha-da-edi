# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20150304_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(verbose_name='editado em', default=datetime.datetime(2015, 3, 4, 18, 3, 7, 345032, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
