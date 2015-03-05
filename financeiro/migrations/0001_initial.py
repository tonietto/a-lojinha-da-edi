# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from decimal import Decimal
import django.db.models.deletion
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='PR', max_length=2)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('nota', models.CharField(choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')], default=3, max_length=1)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('tipo_de_loja', models.CharField(choices=[('R', 'Loja de Rua'), ('S', 'Loja de Shopping')], default=2, max_length=1)),
                ('cnpj', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='CNPJ')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('nota', models.CharField(choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')], default=3, max_length=1)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('nota', models.CharField(choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')], default=3, max_length=1)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('imagem', models.ImageField(upload_to='uploads/imagens/marcas', blank=True)),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parcela',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('numero', models.PositiveSmallIntegerField(default=0, verbose_name='número da parcela')),
                ('data', models.DateField(default=datetime.datetime(2015, 3, 5, 13, 46, 32, 334656, tzinfo=utc))),
                ('valor', models.DecimalField(max_digits=5, default=Decimal('0.00'), validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], decimal_places=2)),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('quantidade', models.PositiveSmallIntegerField(default=1)),
                ('valor_venda', models.DecimalField(max_digits=5, blank=True, decimal_places=2, null=True, verbose_name='valor venda')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
                ('peca', models.ManyToManyField(to='catalogo.Peca', verbose_name='peça')),
                ('tamanhos', models.ManyToManyField(to='catalogo.TamanhoDaPeca')),
            ],
            options={
                'ordering': ('data_de_edicao',),
                'verbose_name': 'peça',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'Romaneio'), ('2', 'Nota Fiscal')], default=1, max_length=1)),
                ('numero', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='número')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('rua', models.CharField(blank=True, max_length=150)),
                ('numero', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='número')),
                ('complemento', models.CharField(null=True, blank=True, max_length=30)),
                ('bairro', models.CharField(blank=True, max_length=30)),
                ('nota', models.CharField(choices=[('0', 'Péssimo'), ('1', 'Ruim'), ('2', 'Regular'), ('3', 'Bom'), ('4', 'Ótimo'), ('5', 'Excelente')], default=3, max_length=1)),
                ('anotacoes', models.TextField(blank=True, verbose_name='anotações')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('data', models.DateField(default=datetime.datetime(2015, 3, 5, 13, 46, 32, 334656, tzinfo=utc))),
                ('forma_de_pagamento', models.CharField(choices=[('DIN', 'dinheiro'), ('CAD', 'caderninho'), ('CAR', 'cartão'), ('PGS', 'PagSeguro')], max_length=3)),
                ('forma_caderninho', models.CharField(max_length=3, choices=[('DIN', 'dinheiro'), ('PAR', 'parcelado'), ('DEP', 'depósito')], blank=True, verbose_name='forma de pagamento no caderninho')),
                ('forma_cartao', models.CharField(max_length=1, choices=[('C', 'crédito'), ('D', 'débito')], blank=True, verbose_name='forma de pagamento no cartão')),
                ('numero_de_parcelas', models.CharField(choices=[('1', '1x'), ('2', '2x'), ('3', '3x'), ('4', '4x')], blank=True, max_length=1)),
                ('status_venda', models.CharField(null=True, choices=[('0', 'aberta'), ('1', 'encerrada')], default=0, blank=True, max_length=1)),
                ('status_peca', models.CharField(null=True, max_length=1, choices=[('0', 'aguardando cliente'), ('1', 'em trânsito'), ('2', 'entregue')], blank=True, verbose_name='status peça')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='abertura')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
                ('data_de_fechamento', models.DateTimeField(blank=True, null=True, verbose_name='fechamento')),
                ('cliente', models.ForeignKey(blank=True, to='cliente.Cliente')),
            ],
            options={
                'ordering': ('data_de_edicao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('data', models.DateField(default=datetime.datetime(2015, 3, 5, 13, 46, 32, 334656, tzinfo=utc))),
                ('custo_combustivel', models.DecimalField(max_digits=5, default=Decimal('0.00'), decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='combustível')),
                ('custo_pedagios', models.DecimalField(max_digits=5, default=Decimal('0.00'), decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='pedágios')),
                ('custo_alimentacao', models.DecimalField(max_digits=5, default=Decimal('0.00'), decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='alimentação')),
                ('custo_estacionamento', models.DecimalField(max_digits=5, default=Decimal('0.00'), decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='estacionamento')),
                ('custo_transporte', models.DecimalField(max_digits=5, default=Decimal('0.00'), decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='transporte')),
                ('custo_hospedagem', models.DecimalField(max_digits=5, default=Decimal('0.00'), decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='hospedagem')),
                ('custo_outros', models.DecimalField(max_digits=5, default=Decimal('0.00'), decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='outros custos')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='cadastro')),
                ('data_de_edicao', models.DateTimeField(auto_now=True, verbose_name='edição')),
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
            field=models.ForeignKey(to='financeiro.Shopping', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guia',
            name='shoppings',
            field=models.ManyToManyField(to='financeiro.Shopping'),
            preserve_default=True,
        ),
    ]
