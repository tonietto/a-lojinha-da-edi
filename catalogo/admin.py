from django.contrib import admin
from catalogo.models import Peca, CategoriaDaPeca, CorDaPeca
from catalogo.models import TamanhoDaPeca, TagsDaPeca


class PecaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': [
                           'nome',
                           'categoria',
                           'tags',
                           ('marca', 'genero', 'cores',),
                           ]}),
        ('Imagens',  {'fields': [
                                'imagem_1',
                                'imagem_2',
                                'imagem_3',
                                'imagem_4'
                                ]}),
        ('Financeiro',  {'fields': [
                                   'recibo',
                                   ('custo_unitario', 'preco_unitario', 'preco_unitario_promocional',),
                                   ]}),
    ]


admin.site.register(Peca, PecaAdmin)
admin.site.register(CategoriaDaPeca)
admin.site.register(CorDaPeca)
admin.site.register(TamanhoDaPeca)
admin.site.register(TagsDaPeca)
