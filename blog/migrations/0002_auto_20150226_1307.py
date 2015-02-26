# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(verbose_name='editado em', default=datetime.datetime(2015, 2, 26, 16, 7, 54, 579496, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='data de publicação', default=datetime.datetime(2015, 2, 26, 16, 7, 54, 579496, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
