# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150302_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 18, 27, 24, 943937, tzinfo=utc), verbose_name='editado em'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 18, 27, 24, 943937, tzinfo=utc), verbose_name='data de publicação'),
            preserve_default=True,
        ),
    ]
