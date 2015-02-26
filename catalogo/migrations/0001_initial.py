# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDaPeca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('categoria', models.CharField(unique=True, default='Nenhuma', max_length=30)),
            ],
            options={
                'verbose_name': 'categoria',
                'ordering': ('categoria',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CorDaPeca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('cor', models.CharField(unique=True, default='Branca', max_length=30)),
                ('codigo', models.CharField(verbose_name='código', help_text='Código HEX da cor. Escolha em http://goo.gl/ZEQ38K. Ex.: #FFFFFF (Branco).', max_length=7, blank=True)),
            ],
            options={
                'verbose_name': 'cor',
                'verbose_name_plural': 'cores',
                'ordering': ('cor',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(default='', max_length=30)),
                ('slug', models.SlugField(help_text='URL. Ex.: blusinha-guardachuvas')),
                ('genero', models.CharField(default='F', max_length=1, choices=[('F', 'Feminino'), ('M', 'Masculino')])),
                ('imagem_1', models.ImageField(upload_to='imagem_de_produto')),
                ('imagem_2', models.ImageField(upload_to='imagem_de_produto', blank=True)),
                ('imagem_3', models.ImageField(upload_to='imagem_de_produto', blank=True)),
                ('imagem_4', models.ImageField(upload_to='imagem_de_produto', blank=True)),
                ('ativa', models.BooleanField(default=True, verbose_name='ativa no site')),
                ('quantidade_comprada', models.PositiveSmallIntegerField(default=1)),
                ('quantidade_em_estoque', models.PositiveSmallIntegerField(default=1)),
                ('reservada', models.BooleanField(default=False)),
                ('custo_unitario', models.DecimalField(default=Decimal('0.00'), verbose_name='custo', decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('preco_unitario', models.DecimalField(default=Decimal('0.00'), verbose_name='preço', decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('preco_unitario_promocional', models.DecimalField(default=Decimal('0.00'), verbose_name='preço promocional', decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de publicacao')),
                ('categoria', models.ForeignKey(to='catalogo.CategoriaDaPeca')),
                ('cores', models.ManyToManyField(to='catalogo.CorDaPeca', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'peça',
                'ordering': ('pub_date', 'nome'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagsDaPeca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tag', models.CharField(unique=True, max_length=30)),
                ('slug', models.SlugField(help_text='URL da tag. Ex.: manga-longa')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
            ],
            options={
                'verbose_name': 'tag(s)',
                'verbose_name_plural': 'tags',
                'ordering': ('pub_date', 'tag'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TamanhoDaPeca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tamanho', models.CharField(unique=True, default='M', max_length=3)),
            ],
            options={
                'verbose_name': 'tamanho',
                'ordering': ('tamanho',),
            },
            bases=(models.Model,),
        ),
    ]
