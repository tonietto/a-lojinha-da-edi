# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_auto_20150226_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, upload_to='foto_do_cliente')),
                ('rua', models.CharField(blank=True, max_length=150)),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número', null=True, blank=True)),
                ('bairro', models.CharField(blank=True, max_length=30)),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade', blank=True)),
            ],
            options={
                'ordering': ('nome', 'pub_date'),
            },
            bases=(models.Model,),
        ),
    ]
