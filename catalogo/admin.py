from django.contrib import admin
from catalogo.models import Peca, CategoriaDaPeca, CorDaPeca
from catalogo.models import TamanhoDaPeca, TagsDaPeca, QuantidadeDePecasPorTamanho


class QuantidadeDePecasPorTamanhoInline(admin.TabularInline):
    model = QuantidadeDePecasPorTamanho
    extra = 1
    classes = ('grp-collapse grp-open',)


class PecaAdmin(admin.ModelAdmin):
    raw_id_fields = ('categoria', 'tags', 'marca', 'cores',)
    autocomplete_lookup_fields = {
        'fk': ['categoria', 'marca'],
        'm2m': ['tags', 'cores'],
    }
    fieldsets = [
        ('Geral',  {
            "classes": ("grp-collapse grp-open",),
            'fields': [
                      'nome',
                      'categoria',
                      'tags',
                      ('marca', 'genero', 'cores',),
                      ]}),
        ("Quantidade Inlines", {"classes": ("placeholder quantidadedepecasportamanho_set-group",), "fields": ()}),
        ('Imagens',  {
            "classes": ("grp-collapse grp-open",),
            'fields': [
                      'imagem_1',
                      'imagem_2',
                      'imagem_3',
                      'imagem_4'
                                ]}),
        ('Financeiro',  {
            "classes": ("grp-collapse grp-open",),
            'fields': [
                      'recibo',
                      'referencia_original',
                      ('custo_unitario', 'preco_unitario', 'preco_unitario_promocional',),
                      ]}),
    ]
    inlines = [QuantidadeDePecasPorTamanhoInline]
    list_display = (
                    'thumbnail',
                    'nome',
                    'categoria',
                    'get_tags',
                    'marca',
                    'genero',
                    'get_cores',
                    'referencia_original',
                    'custo_unitario',
                    'preco_unitario',
                    'preco_unitario_promocional',
                    'lucro_unitario',
                    'data_de_cadastro',
                    'data_de_edicao'
                    )
    search_fields = (
                     'nome',
                     'genero',
                     'referencia_original',
                     'data_de_cadastro',
                     'data_de_edicao',
                     )

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/admin/js/tinymce_setup.js',
        ]


class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
                    'categoria',
                    'data_de_criacao',
                    'data_de_edicao'
                    )
    search_fields = ('categoria',)


class CorAdmin(admin.ModelAdmin):
    list_display = (
                    'cor',
                    'circulo',
                    'data_de_criacao',
                    'data_de_edicao'
                    )
    search_fields = ('cor', 'codigo')


class TagAdmin(admin.ModelAdmin):
    list_display = (
                    'tag',
                    'data_de_criacao',
                    'data_de_edicao'
                    )
    search_fields = ('tag',)


class TamanhoAdmin(admin.ModelAdmin):
    list_display = (
                    'tamanho',
                    'data_de_criacao',
                    'data_de_edicao'
                    )
    search_fields = ('tamanho',)


admin.site.register(Peca, PecaAdmin)
admin.site.register(CategoriaDaPeca, CategoriaAdmin)
admin.site.register(CorDaPeca, CorAdmin)
admin.site.register(TagsDaPeca, TagAdmin)
admin.site.register(TamanhoDaPeca, TamanhoAdmin)
