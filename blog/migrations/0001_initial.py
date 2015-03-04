# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('titulo', models.CharField(verbose_name='título', blank=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('imagem', models.ImageField(upload_to='imagem_do_post')),
                ('texto', models.TextField()),
                ('edicao', models.DateTimeField(verbose_name='editado em', default=datetime.datetime(2015, 3, 4, 20, 11, 7, 489753, tzinfo=utc))),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('categoria', models.ManyToManyField(to='blog.Categoria')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
    ]
