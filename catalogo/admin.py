from django.contrib import admin
from catalogo.models import Peca, CategoriaDaPeca, CorDaPeca
from catalogo.models import TamanhoDaPeca, TagsDaPeca


class PecaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': [
                           ('nome', 'slug',),
                           'categoria',
                           'tags',
                           ('marca', 'tamanho', 'genero', 'cores',),
                           ('quantidade_comprada', 'quantidade_em_estoque',),
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
    prepopulated_fields = {'slug': ('nome',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tag',)}


admin.site.register(Peca, PecaAdmin)
admin.site.register(CategoriaDaPeca)
admin.site.register(CorDaPeca)
admin.site.register(TamanhoDaPeca)
admin.site.register(TagsDaPeca, TagAdmin)
