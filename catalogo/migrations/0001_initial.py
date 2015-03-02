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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('categoria', models.CharField(unique=True, max_length=30)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cor', models.CharField(unique=True, max_length=30)),
                ('codigo', models.CharField(verbose_name='código', blank=True, help_text='Código HEX da cor. Escolha em http://goo.gl/ZEQ38K. Ex.: #FFFFFF (Branco).', max_length=7)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(default='', max_length=30)),
                ('slug', models.SlugField(help_text='URL. Ex.: blusinha-guardachuvas')),
                ('genero', models.CharField(default='F', max_length=1, choices=[('F', 'Feminino'), ('M', 'Masculino')])),
                ('imagem_1', models.ImageField(blank=True, upload_to='imagem_de_produto')),
                ('imagem_2', models.ImageField(blank=True, upload_to='imagem_de_produto')),
                ('imagem_3', models.ImageField(blank=True, upload_to='imagem_de_produto')),
                ('imagem_4', models.ImageField(blank=True, upload_to='imagem_de_produto')),
                ('mostrar_no_site', models.BooleanField(default=True)),
                ('custo_unitario', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, verbose_name='custo', decimal_places=2)),
                ('preco_unitario', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, verbose_name='preço', decimal_places=2)),
                ('preco_unitario_promocional', models.DecimalField(validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], blank=True, max_digits=5, verbose_name='preço promocional', decimal_places=2, default=Decimal('0.00'), null=True)),
                ('pub_date', models.DateTimeField(verbose_name='data de publicacao', auto_now_add=True)),
                ('codigo', models.PositiveSmallIntegerField(verbose_name='código', null=True, db_column='codigo_automatico')),
                ('categoria', models.ForeignKey(to='catalogo.CategoriaDaPeca')),
                ('cores', models.ManyToManyField(null=True, blank=True, to='catalogo.CorDaPeca')),
            ],
            options={
                'verbose_name': 'peça',
                'ordering': ('pub_date', 'nome'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuantidadeDePecasPorTamanho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('quantidade_comprada', models.PositiveSmallIntegerField(default=1)),
                ('quantidade_em_estoque', models.PositiveSmallIntegerField(default=1)),
                ('peca', models.ForeignKey(to='catalogo.Peca')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagsDaPeca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=30)),
                ('slug', models.SlugField(help_text='URL da tag. Ex.: manga-longa')),
                ('pub_date', models.DateTimeField(verbose_name='data de criação', auto_now_add=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tamanho', models.CharField(default='M', unique=True, max_length=3)),
            ],
            options={
                'verbose_name': 'tamanho',
                'ordering': ('tamanho',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='quantidadedepecasportamanho',
            name='tamanho',
            field=models.ForeignKey(to='catalogo.TamanhoDaPeca'),
            preserve_default=True,
        ),
    ]
