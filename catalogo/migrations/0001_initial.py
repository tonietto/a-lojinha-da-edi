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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('categoria', models.CharField(unique=True, max_length=30)),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='criação')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
            ],
            options={
                'ordering': ('data_de_edicao',),
                'verbose_name': 'categoria',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CorDaPeca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('cor', models.CharField(unique=True, max_length=30)),
                ('codigo', models.CharField(help_text='Código HEX da cor. Escolha em http://goo.gl/ZEQ38K. Ex.: #FFFFFF (Branco).', blank=True, max_length=7, verbose_name='código')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='criação')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
            ],
            options={
                'ordering': ('data_de_edicao',),
                'verbose_name_plural': 'cores',
                'verbose_name': 'cor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=60)),
                ('genero', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('imagem_1', models.ImageField(upload_to='uploads/imagens/pecas/', blank=True)),
                ('imagem_2', models.ImageField(upload_to='uploads/imagens/pecas/', blank=True)),
                ('imagem_3', models.ImageField(upload_to='uploads/imagens/pecas/', blank=True)),
                ('imagem_4', models.ImageField(upload_to='uploads/imagens/pecas/', blank=True)),
                ('mostrar_no_site', models.BooleanField(default=True)),
                ('referencia_original', models.CharField(null=True, blank=True, max_length=30, verbose_name='referência original')),
                ('custo_unitario', models.DecimalField(max_digits=5, default=Decimal('0.00'), decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='custo R$')),
                ('preco_unitario', models.DecimalField(max_digits=5, default=Decimal('0.00'), decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='preço R$')),
                ('preco_unitario_promocional', models.DecimalField(decimal_places=2, verbose_name='promoção R$', max_digits=5, null=True, blank=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
                ('categoria', models.ForeignKey(to='catalogo.CategoriaDaPeca')),
                ('cores', models.ManyToManyField(blank=True, null=True, to='catalogo.CorDaPeca')),
            ],
            options={
                'ordering': ('data_de_edicao',),
                'verbose_name': 'peça',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuantidadeDePecasPorTamanho',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='criação')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('tag', models.CharField(unique=True, max_length=30)),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='criação')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
            ],
            options={
                'ordering': ('data_de_edicao',),
                'verbose_name_plural': 'tags das peças',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TamanhoDaPeca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('tamanho', models.CharField(unique=True, max_length=3)),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='criação')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
            ],
            options={
                'ordering': ('data_de_edicao',),
                'verbose_name': 'tamanho',
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
