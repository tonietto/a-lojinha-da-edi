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
                      ('custo_unitario', 'preco_unitario', 'preco_unitario_promocional',),
                      ]}),
    ]
    inlines = [QuantidadeDePecasPorTamanhoInline]

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/admin/js/tinymce_setup.js',
        ]


admin.site.register(Peca, PecaAdmin)
admin.site.register(CategoriaDaPeca)
admin.site.register(CorDaPeca)
admin.site.register(TamanhoDaPeca)
admin.site.register(TagsDaPeca)
