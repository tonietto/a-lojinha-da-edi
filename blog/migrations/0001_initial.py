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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('titulo', models.CharField(max_length=100, blank=True, verbose_name='título')),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('imagem', models.ImageField(upload_to='imagem_do_post')),
                ('texto', models.TextField()),
                ('edicao', models.DateTimeField(default=datetime.datetime(2015, 2, 26, 15, 47, 50, 975467, tzinfo=utc), verbose_name='editado em')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 2, 26, 15, 47, 50, 975467, tzinfo=utc), verbose_name='data de publicação')),
                ('categoria', models.ManyToManyField(to='blog.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
