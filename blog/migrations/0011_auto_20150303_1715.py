# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150303_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 20, 15, 14, 368929, tzinfo=utc), verbose_name='editado em'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 20, 15, 14, 368929, tzinfo=utc), verbose_name='data de publicação'),
            preserve_default=True,
        ),
    ]
