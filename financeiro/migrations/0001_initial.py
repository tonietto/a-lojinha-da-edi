# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators
from django.utils.timezone import utc
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(default='PR', max_length=2, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
            ],
            options={
                'ordering': ('cidade', 'pub_date'),
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
                ('nota', models.CharField(default=3, max_length=1, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')])),
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
                ('tipo_de_loja', models.CharField(default=2, max_length=1, choices=[('R', 'Loja de Rua'), ('S', 'Loja de Shopping')])),
                ('cnpj', models.PositiveSmallIntegerField(verbose_name='CNPJ', null=True, blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('nota', models.CharField(default=3, max_length=1, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')])),
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
                ('nota', models.CharField(default=3, max_length=1, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')])),
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
            name='Parcela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('numero', models.PositiveSmallIntegerField(default=0, verbose_name='número da parcela')),
                ('data', models.DateField(default=datetime.datetime(2015, 3, 2, 13, 2, 30, 465699, tzinfo=utc))),
                ('valor', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('quantidade', models.PositiveSmallIntegerField(default=1)),
                ('valor_venda', models.DecimalField(verbose_name='valor venda', decimal_places=2, null=True, blank=True, max_digits=5)),
                ('peca', models.ManyToManyField(verbose_name='peça', to='catalogo.Peca')),
            ],
            options={
                'verbose_name': 'peça',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tipo', models.CharField(default=1, max_length=1, choices=[('1', 'Romaneio'), ('2', 'Nota Fiscal')])),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número', null=True, blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
                ('loja', models.ForeignKey(to='financeiro.Loja')),
            ],
            options={
                'ordering': ('pub_date',),
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
                ('nota', models.CharField(default=3, max_length=1, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')])),
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
                ('data', models.DateField(default=datetime.datetime(2015, 3, 2, 13, 2, 30, 465699, tzinfo=utc))),
                ('forma_de_pagamento', models.CharField(default='DIN', max_length=3, choices=[('DIN', 'dinheiro'), ('CAD', 'caderninho'), ('CAR', 'cartão'), ('PGS', 'PagSeguro')])),
                ('forma_caderninho', models.CharField(default='PAR', verbose_name='forma de pagamento no caderninho', blank=True, max_length=3, choices=[('DIN', 'dinheiro'), ('PAR', 'parcelado'), ('DEP', 'depósito')])),
                ('forma_cartao', models.CharField(default='C', verbose_name='forma de pagamento no cartão', blank=True, max_length=1, choices=[('C', 'crédito'), ('D', 'débito')])),
                ('numero_de_parcelas', models.CharField(default='2', blank=True, max_length=1, choices=[('1', '1x'), ('2', '2x'), ('3', '3x'), ('4', '4x')])),
                ('pub_date', models.DateTimeField(verbose_name='data de cadastro', auto_now_add=True)),
                ('cliente', models.ForeignKey(blank=True, to='cliente.Cliente')),
            ],
            options={
                'ordering': ('data', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('data', models.DateField(default=datetime.datetime(2015, 3, 2, 13, 2, 30, 465699, tzinfo=utc))),
                ('custo_combustivel', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, verbose_name='combustível', decimal_places=2)),
                ('custo_pedagios', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, verbose_name='pedágios', decimal_places=2)),
                ('custo_alimentacao', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, verbose_name='alimentação', decimal_places=2)),
                ('custo_estacionamento', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, verbose_name='estacionamento', decimal_places=2)),
                ('custo_transporte', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, verbose_name='transporte', decimal_places=2)),
                ('custo_hospedagem', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, verbose_name='hospedagem', decimal_places=2)),
                ('custo_outros', models.DecimalField(default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], max_digits=5, verbose_name='outros custos', decimal_places=2)),
                ('pub_date', models.DateTimeField(verbose_name='data de publicacao', auto_now_add=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'verbose_name_plural': 'viagens',
                'ordering': ('data', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recibo',
            name='viagem',
            field=models.ForeignKey(to='financeiro.Viagem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='peca',
            name='venda',
            field=models.ForeignKey(to='financeiro.Venda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parcela',
            name='venda',
            field=models.ForeignKey(to='financeiro.Venda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loja',
            name='shopping',
            field=models.ForeignKey(blank=True, to='financeiro.Shopping', on_delete=django.db.models.deletion.SET_NULL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guia',
            name='shoppings',
            field=models.ManyToManyField(to='financeiro.Shopping'),
            preserve_default=True,
        ),
    ]
