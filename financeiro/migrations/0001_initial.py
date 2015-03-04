# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators
from django.utils.timezone import utc
import datetime
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(default='PR', max_length=2, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('nota', models.CharField(default=3, max_length=1, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')])),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('tipo_de_loja', models.CharField(default=2, max_length=1, choices=[('R', 'Loja de Rua'), ('S', 'Loja de Shopping')])),
                ('cnpj', models.PositiveSmallIntegerField(verbose_name='CNPJ', null=True, blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('nota', models.CharField(default=3, max_length=1, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')])),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('nota', models.CharField(default=3, max_length=1, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')])),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('imagem', models.ImageField(upload_to='uploads/imagens/marcas', blank=True)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parcela',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número da parcela', default=0)),
                ('data', models.DateField(default=datetime.datetime(2015, 3, 4, 20, 11, 7, 503499, tzinfo=utc))),
                ('valor', models.DecimalField(validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('quantidade', models.PositiveSmallIntegerField(default=1)),
                ('valor_venda', models.DecimalField(verbose_name='valor venda', null=True, blank=True, max_digits=5, decimal_places=2)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('peca', models.ManyToManyField(verbose_name='peça', to='catalogo.Peca')),
                ('tamanhos', models.ManyToManyField(to='catalogo.QuantidadeDePecasPorTamanho')),
            ],
            options={
                'verbose_name': 'peça',
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tipo', models.CharField(default=1, max_length=1, choices=[('1', 'Romaneio'), ('2', 'Nota Fiscal')])),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número', null=True, blank=True)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('loja', models.ForeignKey(to='financeiro.Loja')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('rua', models.CharField(blank=True, max_length=150)),
                ('numero', models.PositiveSmallIntegerField(verbose_name='número', null=True, blank=True)),
                ('complemento', models.CharField(null=True, blank=True, max_length=30)),
                ('bairro', models.CharField(blank=True, max_length=30)),
                ('nota', models.CharField(default=3, max_length=1, choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')])),
                ('anotacoes', models.TextField(verbose_name='anotações', blank=True)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('data', models.DateField(default=datetime.datetime(2015, 3, 4, 20, 11, 7, 503499, tzinfo=utc))),
                ('forma_de_pagamento', models.CharField(default='DIN', max_length=3, choices=[('DIN', 'dinheiro'), ('CAD', 'caderninho'), ('CAR', 'cartão'), ('PGS', 'PagSeguro')])),
                ('forma_caderninho', models.CharField(verbose_name='forma de pagamento no caderninho', default='PAR', blank=True, max_length=3, choices=[('DIN', 'dinheiro'), ('PAR', 'parcelado'), ('DEP', 'depósito')])),
                ('forma_cartao', models.CharField(verbose_name='forma de pagamento no cartão', default='C', blank=True, max_length=1, choices=[('C', 'crédito'), ('D', 'débito')])),
                ('numero_de_parcelas', models.CharField(default='2', blank=True, max_length=1, choices=[('1', '1x'), ('2', '2x'), ('3', '3x'), ('4', '4x')])),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('cliente', models.ForeignKey(to='cliente.Cliente', blank=True)),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('data', models.DateField(default=datetime.datetime(2015, 3, 4, 20, 11, 7, 503499, tzinfo=utc))),
                ('custo_combustivel', models.DecimalField(verbose_name='combustível', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('custo_pedagios', models.DecimalField(verbose_name='pedágios', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('custo_alimentacao', models.DecimalField(verbose_name='alimentação', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('custo_estacionamento', models.DecimalField(verbose_name='estacionamento', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('custo_transporte', models.DecimalField(verbose_name='transporte', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('custo_hospedagem', models.DecimalField(verbose_name='hospedagem', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('custo_outros', models.DecimalField(verbose_name='outros custos', validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'), decimal_places=2, max_digits=5)),
                ('data_de_cadastro', models.DateTimeField(verbose_name='cadastro', auto_now_add=True)),
                ('data_de_edicao', models.DateTimeField(verbose_name='edição', auto_now=True)),
                ('cidade', models.ForeignKey(to='financeiro.Cidade')),
            ],
            options={
                'ordering': ('data_de_edicao',),
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
            field=models.ForeignKey(null=True, to='financeiro.Shopping', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guia',
            name='shoppings',
            field=models.ManyToManyField(to='financeiro.Shopping'),
            preserve_default=True,
        ),
    ]
