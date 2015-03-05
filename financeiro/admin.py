from django.contrib import admin
from financeiro.models import Cidade, Shopping, Guia, Loja, Marca, Viagem
from financeiro.models import Recibo, Venda, Peca, Parcela


class ViagemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Geral', {
            "classes": ("grp-collapse grp-open",),
            'fields': [
                       'data',
                       'cidade',
                       ]}),
        ('Custos', {
            "classes": ("grp-collapse grp-open",),
            'fields': [
                       'custo_combustivel',
                       'custo_pedagios',
                       'custo_alimentacao',
                       'custo_estacionamento',
                       'custo_transporte',
                       'custo_hospedagem',
                       'custo_outros'
                       ]}),
    ]
    list_display = (
                    'cidade',
                    'data',
                    'combustivel',
                    'pedagios',
                    'alimentacao',
                    'estacionamento',
                    'transporte',
                    'hospedagem',
                    'outros',
                    'custo_total'
                    )
    search_fields = ['cidade']


class PecaInline(admin.TabularInline):
    raw_id_fields = ('peca', 'tamanhos')
    autocomplete_lookup_fields = {
        'm2m': ['peca', 'tamanhos', ],
    }
    model = Peca
    extra = 1


class ParcelaInline(admin.TabularInline):
    model = Parcela
    max_num = 4
    extra = 0


class VendaAdmin(admin.ModelAdmin):
    raw_id_fields = ('cliente',)
    autocomplete_lookup_fields = {
        'fk': ['cliente', ],
    }
    fieldsets = [
        (None, {
            "classes": ("grp-collapse grp-open",),
            'fields': [
                       'cliente',
                       'data',
                       'forma_de_pagamento',
                       'forma_caderninho',
                       'forma_cartao',
                       'numero_de_parcelas',
                       'status_venda',
                       'status_peca',
                       ]}),
    ]
    inlines = [PecaInline, ParcelaInline]
    list_display = (
                    'cliente',
                    'data',
                    'forma_de_pagamento',
                    'forma_caderninho',
                    'forma_cartao',
                    'numero_de_parcelas',
                    'data_de_cadastro',
                    'data_de_edicao',
                    )


class CidadeAdmin(admin.ModelAdmin):
    list_display = (
                    'cidade',
                    'estado',
                    'data_de_cadastro',
                    'data_de_edicao',
                    )
    search_fields = (
                    'cidade',
                    'estado',
                    'anotacoes',
                    )


class GuiaAdmin(admin.ModelAdmin):
    raw_id_fields = ('cidade', 'shoppings')
    autocomplete_lookup_fields = {
        'fk': ['cidade'],
        'm2m': ['shoppings'],
    }
    list_display = (
                    'nome_completo',
                    'cidade',
                    'get_telefone',
                    'email',
                    'get_shoppings',
                    'nota',
                    'data_de_cadastro',
                    'data_de_edicao',
                    )
    search_fields = (
                    'nome',
                    'sobrenome',
                    'telefone',
                    'email',
                    'nota',
                    'data_de_cadastro',
                    'data_de_edicao',
                    )


class ShoppingAdmin(admin.ModelAdmin):
    raw_id_fields = ('cidade',)
    autocomplete_lookup_fields = {
        'fk': ['cidade'],
    }
    list_display = (
                    'nome',
                    'endereco',
                    'nota',
                    'data_de_cadastro',
                    'data_de_edicao',
                    )
    search_fields = (
                    'nome',
                    'rua',
                    'numero',
                    'bairro',
                    'nota',
                    'anotacoes',
                    )


class LojaAdmin(admin.ModelAdmin):
    raw_id_fields = ('cidade', 'shopping')
    autocomplete_lookup_fields = {
        'fk': ['cidade', 'shopping'],
    }
    list_display = (
                    'nome',
                    'tipo_de_loja',
                    'shopping',
                    'get_cnpj',
                    'cidade',
                    'email',
                    'get_telefone',
                    'nota',
                    'data_de_cadastro',
                    'data_de_edicao',
                    )
    search_fields = (
                    'nome',
                    'tipo_de_loja',
                    'cnpj',
                    'email',
                    'telefone',
                    'nota',
                    'anotacoes',
                    )


class MarcaAdmin(admin.ModelAdmin):
    list_display = (
                    'nome',
                    'nota',
                    'data_de_cadastro',
                    'data_de_edicao',
                    )
    search_fields = ('nome', 'nota',)


class ReciboAdmin(admin.ModelAdmin):
    raw_id_fields = ('viagem',)
    autocomplete_lookup_fields = {
        'fk': ['viagem', ],
    }
    list_display = (
                    '__str__',
                    'tipo',
                    'numero',
                    'data_de_cadastro',
                    'data_de_edicao',
                    )
    search_fields = ('tipo', 'numero',)

admin.site.register(Viagem, ViagemAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Guia, GuiaAdmin)
admin.site.register(Shopping, ShoppingAdmin)
admin.site.register(Loja, LojaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Recibo, ReciboAdmin)
admin.site.register(Venda, VendaAdmin)
