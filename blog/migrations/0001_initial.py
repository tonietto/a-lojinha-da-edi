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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, verbose_name='título')),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('imagem', models.ImageField(upload_to='imagem_do_post')),
                ('texto', models.TextField()),
                ('edicao', models.DateTimeField(default=datetime.datetime(2015, 3, 5, 13, 46, 32, 319891, tzinfo=utc), verbose_name='editado em')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
                ('categoria', models.ManyToManyField(to='blog.Categoria')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
    ]
