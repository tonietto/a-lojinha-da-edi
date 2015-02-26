# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDaPeca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('categoria', models.CharField(default='Nenhuma', unique=True, max_length=30)),
            ],
            options={
                'ordering': ('categoria',),
                'verbose_name': 'categoria',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CorDaPeca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('cor', models.CharField(default='Branca', unique=True, max_length=30)),
                ('codigo', models.CharField(help_text='Código HEX da cor. Escolha em http://goo.gl/ZEQ38K. Ex.: #FFFFFF (Branco).', blank=True, verbose_name='código', max_length=7)),
            ],
            options={
                'ordering': ('cor',),
                'verbose_name_plural': 'cores',
                'verbose_name': 'cor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(default='', max_length=30)),
                ('slug', models.SlugField(help_text='URL. Ex.: blusinha-guardachuvas')),
                ('genero', models.CharField(default='F', choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1)),
                ('imagem_1', models.ImageField(upload_to='imagem_de_produto')),
                ('imagem_2', models.ImageField(upload_to='imagem_de_produto', blank=True)),
                ('imagem_3', models.ImageField(upload_to='imagem_de_produto', blank=True)),
                ('imagem_4', models.ImageField(upload_to='imagem_de_produto', blank=True)),
                ('ativa', models.BooleanField(default=True, verbose_name='ativa no site')),
                ('quantidade_comprada', models.PositiveSmallIntegerField(default=1)),
                ('quantidade_em_estoque', models.PositiveSmallIntegerField(default=1)),
                ('reservada', models.BooleanField(default=False)),
                ('custo_unitario', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='custo', max_digits=5)),
                ('preco_unitario', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='preço', max_digits=5)),
                ('preco_unitario_promocional', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='preço promocional', max_digits=5)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de publicacao')),
                ('categoria', models.ForeignKey(to='catalogo.CategoriaDaPeca')),
                ('cores', models.ManyToManyField(null=True, blank=True, to='catalogo.CorDaPeca')),
            ],
            options={
                'ordering': ('pub_date', 'nome'),
                'verbose_name': 'peça',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagsDaPeca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=30)),
                ('slug', models.SlugField(help_text='URL da tag. Ex.: manga-longa')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
            ],
            options={
                'ordering': ('pub_date', 'tag'),
                'verbose_name_plural': 'tags',
                'verbose_name': 'tag(s)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TamanhoDaPeca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tamanho', models.CharField(default='M', unique=True, max_length=3)),
            ],
            options={
                'ordering': ('tamanho',),
                'verbose_name': 'tamanho',
            },
            bases=(models.Model,),
        ),
    ]
