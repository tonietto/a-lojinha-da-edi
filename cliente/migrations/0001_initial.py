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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('foto', models.ImageField(upload_to='foto_do_cliente', blank=True)),
                ('rua', models.CharField(blank=True, max_length=150)),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número', null=True, blank=True)),
                ('complemento', models.CharField(null=True, blank=True, max_length=30)),
                ('bairro', models.CharField(blank=True, max_length=30)),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
            ],
            options={
                'ordering': ('data_de_edicao', 'nome'),
            },
            bases=(models.Model,),
        ),
    ]
