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
    search_fields = [ 'cidade' ]


class PecaInline(admin.TabularInline):
    model = Peca
    extra = 1


class ParcelaInline(admin.TabularInline):
    model = Parcela
    max_num = 4
    extra = 0


class VendaAdmin(admin.ModelAdmin):
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
                       ]}),
    ]
    inlines = [PecaInline, ParcelaInline]


admin.site.register(Viagem, ViagemAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Cidade)
admin.site.register(Shopping)
admin.site.register(Guia)
admin.site.register(Loja)
admin.site.register(Marca)
admin.site.register(Recibo)
