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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('foto', models.ImageField(upload_to='foto_do_cliente', blank=True)),
                ('rua', models.CharField(blank=True, max_length=150)),
                ('numero', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='número')),
                ('complemento', models.CharField(null=True, blank=True, max_length=30)),
                ('bairro', models.CharField(blank=True, max_length=30)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
            ],
            options={
                'ordering': ('data_de_edicao', 'nome'),
            },
            bases=(models.Model,),
        ),
    ]
