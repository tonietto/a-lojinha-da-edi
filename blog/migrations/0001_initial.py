# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('titulo', models.CharField(verbose_name='título', blank=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('imagem', models.ImageField(upload_to='imagem_do_post')),
                ('texto', models.TextField()),
                ('edicao', models.DateTimeField(default=datetime.datetime(2015, 3, 2, 13, 2, 30, 452854, tzinfo=utc), verbose_name='editado em')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 3, 2, 13, 2, 30, 452854, tzinfo=utc), verbose_name='data de publicação')),
                ('categoria', models.ManyToManyField(to='blog.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
