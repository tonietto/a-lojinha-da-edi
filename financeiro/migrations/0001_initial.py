# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django.core.validators
import datetime
from decimal import Decimal
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(default='PR', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
            options={
                'ordering': ('cidade', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('nota', models.CharField(default=3, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')], max_length=1)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('tipo_de_loja', models.CharField(default=2, choices=[('R', 'Loja de Rua'), ('S', 'Loja de Shopping')], max_length=1)),
                ('cnpj', models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='CNPJ')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('nota', models.CharField(default=3, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')], max_length=1)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('nota', models.CharField(default=3, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')], max_length=1)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('imagem', models.ImageField(upload_to='imagem_da_marca', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
            options={
                'ordering': ('nome', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parcela',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('numero', models.PositiveSmallIntegerField(default=0, verbose_name='número da parcela')),
                ('data', models.DateField(default=datetime.datetime(2015, 2, 26, 14, 42, 28, 914044, tzinfo=utc))),
                ('valor', models.DecimalField(validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('quantidade', models.PositiveSmallIntegerField(default=1)),
                ('valor_venda', models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=5, verbose_name='valor venda')),
                ('peca', models.ManyToManyField(to='catalogo.Peca', verbose_name='peça')),
            ],
            options={
                'verbose_name': 'peça',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tipo', models.PositiveSmallIntegerField(default=1, choices=[('1', 'Romaneio'), ('2', 'Nota Fiscal')])),
                ('numero', models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='número')),
                ('data', models.DateField(default=datetime.datetime(2015, 2, 26, 14, 42, 28, 914044, tzinfo=utc))),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')),
                ('loja', models.ForeignKey(to='financeiro.Loja')),
            ],
            options={
                'ordering': ('data', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('rua', models.CharField(blank=True, max_length=150)),
                ('numero', models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='número')),
                ('bairro', models.CharField(blank=True, max_length=30)),
                ('nota', models.CharField(default=3, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')], max_length=1)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('cliente', models.CharField(default='', blank=True, max_length=250)),
                ('data', models.DateField(default=datetime.datetime(2015, 2, 26, 14, 42, 28, 914044, tzinfo=utc))),
                ('forma_de_pagamento', models.CharField(default='DIN', choices=[('DIN', 'dinheiro'), ('CAD', 'caderninho'), ('CAR', 'cartão'), ('PGS', 'PagSeguro')], max_length=3)),
                ('forma_caderninho', models.CharField(choices=[('DIN', 'dinheiro'), ('PAR', 'parcelado'), ('DEP', 'depósito')], default='PAR', blank=True, verbose_name='forma de pagamento no caderninho', max_length=3)),
                ('forma_cartao', models.CharField(choices=[('C', 'crédito'), ('D', 'débito')], default='C', blank=True, verbose_name='forma de pagamento no cartão', max_length=1)),
                ('numero_de_parcelas', models.CharField(default='2', blank=True, choices=[('1', '1x'), ('2', '2x'), ('3', '3x'), ('4', '4x')], max_length=1)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
            options={
                'ordering': ('data', 'pub_date'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('data', models.DateField(default=datetime.datetime(2015, 2, 26, 14, 42, 28, 914044, tzinfo=utc))),
                ('custo_combustivel', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='combustível', max_digits=5)),
                ('custo_pedagios', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='pedágios', max_digits=5)),
                ('custo_alimentacao', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='alimentação', max_digits=5)),
                ('custo_estacionamento', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='estacionamento', max_digits=5)),
                ('custo_transporte', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='transporte', max_digits=5)),
                ('custo_hospedagem', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='hospedagem', max_digits=5)),
                ('custo_outros', models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), verbose_name='outros custos', max_digits=5)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='data de publicacao')),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'ordering': ('data', 'pub_date'),
                'verbose_name_plural': 'viagens',
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
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='financeiro.Shopping'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guia',
            name='shoppings',
            field=models.ManyToManyField(to='financeiro.Shopping'),
            preserve_default=True,
        ),
    ]
