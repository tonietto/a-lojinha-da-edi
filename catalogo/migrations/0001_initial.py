# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDaPeca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('categoria', models.CharField(default='Nenhuma', unique=True, max_length=30)),
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
                ('cor', models.CharField(default='Branca', unique=True, max_length=30)),
                ('codigo', models.CharField(verbose_name='código', blank=True, max_length=7, help_text='Código HEX da cor. Escolha em http://goo.gl/ZEQ38K. Ex.: #FFFFFF (Branco).')),
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
                ('genero', models.CharField(default='F', choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1)),
                ('imagem_1', models.ImageField(upload_to='imagem_do_produto')),
                ('imagem_2', models.ImageField(blank=True, upload_to='imagem_do_produto')),
                ('imagem_3', models.ImageField(blank=True, upload_to='imagem_do_produto')),
                ('imagem_4', models.ImageField(blank=True, upload_to='foto_do_produto')),
                ('ativa', models.BooleanField(verbose_name='ativa no site', default=True)),
                ('quantidade_comprada', models.PositiveSmallIntegerField(default=1)),
                ('quantidade_em_estoque', models.PositiveSmallIntegerField(default=1)),
                ('reservada', models.BooleanField(default=False)),
                ('custo_unitario', models.DecimalField(verbose_name='custo', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('preco_unitario', models.DecimalField(verbose_name='preço', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('preco_unitario_promocional', models.DecimalField(verbose_name='preço promocional', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('valor_venda', models.DecimalField(verbose_name='valor venda', null=True, max_digits=5, blank=True, decimal_places=2)),
                ('pub_date', models.DateTimeField(verbose_name='data de publicacao', auto_now_add=True)),
                ('categoria', models.ForeignKey(to='catalogo.CategoriaDaPeca')),
                ('cor', models.ForeignKey(blank=True, to='catalogo.CorDaPeca', null=True)),
                ('marca', models.ForeignKey(to='financeiro.Marca')),
                ('nota_fiscal', models.ForeignKey(blank=True, to='financeiro.NotaFiscal', null=True)),
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
            model_name='peca',
            name='tags',
            field=models.ManyToManyField(related_name='nome', to='catalogo.TagsDaPeca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='peca',
            name='tamanho',
            field=models.ForeignKey(to='catalogo.TamanhoDaPeca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='peca',
            name='venda',
            field=models.ForeignKey(blank=True, to='financeiro.Venda', null=True),
            preserve_default=True,
        ),
    ]
