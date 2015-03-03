# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150303_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 20, 30, 52, 973823, tzinfo=utc), verbose_name='editado em'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 20, 30, 52, 973823, tzinfo=utc), verbose_name='data de publicação'),
            preserve_default=True,
        ),
    ]
