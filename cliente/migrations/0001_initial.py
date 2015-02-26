# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('telefone', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('foto', models.ImageField(upload_to='foto_do_cliente', blank=True)),
                ('rua', models.CharField(max_length=150, blank=True)),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número', null=True, blank=True)),
                ('bairro', models.CharField(max_length=30, blank=True)),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
            options={
                'ordering': ('nome', 'pub_date'),
            },
            bases=(models.Model,),
        ),
    ]
