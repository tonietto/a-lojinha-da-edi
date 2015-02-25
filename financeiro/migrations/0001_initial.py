# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from decimal import Decimal
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2, help_text='Sigla do Estado.')),
                ('pais', models.CharField(verbose_name='país', default='Brasil', max_length=30)),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('nota', models.CharField(default=1, choices=[('0', 'Péssimo'), ('1', 'Regular'), ('2', 'Bom'), ('3', 'Ótimo')], max_length=1)),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'ordering': ('nome', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('tipo_de_loja', models.CharField(default=2, choices=[('R', 'Loja de Rua'), ('S', 'Loja de Shopping')], max_length=1)),
                ('cnpj', models.PositiveSmallIntegerField(verbose_name='CNPJ', null=True, blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('nota', models.CharField(default=1, choices=[('0', 'Péssimo'), ('1', 'Regular'), ('2', 'Bom'), ('3', 'Ótimo')], max_length=1)),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'ordering': ('nome', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('nota', models.CharField(default=1, choices=[('0', 'Péssimo'), ('1', 'Regular'), ('2', 'Bom'), ('3', 'Ótimo')], max_length=1)),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('imagem', models.ImageField(blank=True, upload_to='imagem_da_marca')),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
            ],
            options={
                'ordering': ('nome', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número')),
                ('data_da_nota', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
                ('loja', models.ForeignKey(to='financeiro.Loja')),
            ],
            options={
                'verbose_name_plural': 'Notas Fiscais',
                'ordering': ('data_da_nota', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('rua', models.CharField(blank=True, max_length=150)),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número', null=True, blank=True)),
                ('bairro', models.CharField(blank=True, max_length=30)),
                ('nota', models.CharField(default=1, choices=[('0', 'Péssimo'), ('1', 'Regular'), ('2', 'Bom'), ('3', 'Ótimo')], max_length=1)),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'ordering': ('nome', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('numero_da_venda', models.PositiveSmallIntegerField(verbose_name='número da venda', unique=True)),
                ('cliente', models.CharField(blank=True, max_length=250, default='')),
                ('data_da_venda', models.DateTimeField(auto_now_add=True)),
                ('forma_de_pagamento', models.CharField(default='DIN', choices=[('DIN', 'dinheiro'), ('CAD', 'caderninho'), ('CAR', 'cartão')], max_length=3)),
                ('forma_caderninho', models.CharField(verbose_name='forma de pagamento no caderninho', blank=True, choices=[('DIN', 'dinheiro'), ('PAR', 'parcelado'), ('DEP', 'depósito')], max_length=3, default='PAR')),
                ('forma_cartao', models.CharField(verbose_name='forma de pagamento no cartão', blank=True, choices=[('C', 'crédito'), ('D', 'débito')], max_length=1, default='C')),
                ('numero_de_parcelas', models.CharField(blank=True, choices=[('1', '1x'), ('2', '2x'), ('3', '3x'), ('4', '4x')], max_length=1, default='2')),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
            ],
            options={
                'ordering': ('data_da_venda', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('data', models.DateTimeField(verbose_name='data da viagem', auto_now_add=True)),
                ('custo_combustivel', models.DecimalField(verbose_name='combustível', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('custo_pedagios', models.DecimalField(verbose_name='pedágios', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('custo_alimentacao', models.DecimalField(verbose_name='alimentação', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('custo_estacionamento', models.DecimalField(verbose_name='estacionamento', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('custo_transporte', models.DecimalField(verbose_name='transporte', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('custo_hospedagem', models.DecimalField(verbose_name='hospedagem', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('custo_outros', models.DecimalField(verbose_name='outros custos', decimal_places=2, max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('pub_date', models.DateTimeField(verbose_name='data de publicacao', auto_now_add=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'ordering': ('nome', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notafiscal',
            name='viagem',
            field=models.ForeignKey(to='financeiro.Viagem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loja',
            name='shopping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='financeiro.Shopping', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guia',
            name='shoppings',
            field=models.ManyToManyField(to='financeiro.Shopping'),
            preserve_default=True,
        ),
    ]
