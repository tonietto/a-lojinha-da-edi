# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150303_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('data_de_edicao',)},
        ),
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='categoria',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 12, 59, 28, 264546, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 12, 59, 41, 933697, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='data_de_cadastro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='cadastro', default=datetime.datetime(2015, 3, 4, 13, 0, 4, 725816, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='data_de_edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='edição', default=datetime.datetime(2015, 3, 4, 13, 0, 6, 357831, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='edicao',
            field=models.DateTimeField(verbose_name='editado em', default=datetime.datetime(2015, 3, 4, 12, 58, 55, 99553, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
