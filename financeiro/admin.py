from django.contrib import admin
from financeiro.models import Cidade, Shopping, Guia, Loja, Marca, Viagem
from financeiro.models import NotaFiscal, Venda


class ViagemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': [
                            'nome',
                            'data_da_viagem',
                            'cidade',
                            ]}),
        ('Custos',  {'fields': [
                               'custo_combustivel',
                               'custo_pedagios',
                               'custo_alimentacao',
                               'custo_estacionamento',
                               'custo_transporte',
                               'custo_hospedagem',
                               'custo_outros'
                               ]}),
    ]

admin.site.register(Viagem, ViagemAdmin)
admin.site.register(Cidade)
admin.site.register(Shopping)
admin.site.register(Guia)
admin.site.register(Loja)
admin.site.register(Marca)
admin.site.register(NotaFiscal)
admin.site.register(Venda)
