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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('categoria', models.CharField(unique=True, max_length=30)),
                ('data_de_criacao', models.DateTimeField(verbose_name='criação', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CorDaPeca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cor', models.CharField(unique=True, max_length=30)),
                ('codigo', models.CharField(verbose_name='código', blank=True, max_length=7, help_text='Código HEX da cor. Escolha em http://goo.gl/ZEQ38K. Ex.: #FFFFFF (Branco).')),
                ('data_de_criacao', models.DateTimeField(verbose_name='criação', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
            ],
            options={
                'verbose_name': 'cor',
                'ordering': ('data_de_edicao',),
                'verbose_name_plural': 'cores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(default='', max_length=60)),
                ('genero', models.CharField(default='F', max_length=1, choices=[('F', 'Feminino'), ('M', 'Masculino')])),
                ('imagem_1', models.ImageField(upload_to='uploads/imagens/pecas/', blank=True)),
                ('imagem_2', models.ImageField(upload_to='uploads/imagens/pecas/', blank=True)),
                ('imagem_3', models.ImageField(upload_to='uploads/imagens/pecas/', blank=True)),
                ('imagem_4', models.ImageField(upload_to='uploads/imagens/pecas/', blank=True)),
                ('mostrar_no_site', models.BooleanField(default=True)),
                ('custo_unitario', models.DecimalField(verbose_name='custo R$', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('preco_unitario', models.DecimalField(verbose_name='preço R$', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('preco_unitario_promocional', models.DecimalField(null=True, max_digits=5, decimal_places=2, verbose_name='promoção R$', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], blank=True)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('categoria', models.ForeignKey(to='catalogo.CategoriaDaPeca')),
                ('cores', models.ManyToManyField(null=True, to='catalogo.CorDaPeca', blank=True)),
            ],
            options={
                'verbose_name': 'peça',
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuantidadeDePecasPorTamanho',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('data_de_criacao', models.DateTimeField(verbose_name='criação', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('quantidade_comprada', models.PositiveSmallIntegerField(default=0)),
                ('quantidade_em_estoque', models.PositiveSmallIntegerField(default=0)),
                ('id_peca', models.ForeignKey(to='catalogo.Peca')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagsDaPeca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tag', models.CharField(unique=True, max_length=30)),
                ('data_de_criacao', models.DateTimeField(verbose_name='criação', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TamanhoDaPeca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tamanho', models.CharField(unique=True, max_length=3)),
                ('data_de_criacao', models.DateTimeField(verbose_name='criação', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
            ],
            options={
                'verbose_name': 'tamanho',
                'ordering': ('data_de_edicao',),
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
