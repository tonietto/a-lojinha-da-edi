from django.contrib import admin
from cliente.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    raw_id_fields = ('cidade',)
    autocomplete_lookup_fields = {
        'fk': ['cidade'],
    }
    list_display = (
                    'nome_completo',
                    'get_telefone',
                    'email',
                    'endereco',
                    )
    search_fields = (
                     'nome',
                     'sobrenome',
                     'email',
                     'telefone',
                     'foto',
                     'rua',
                     'numero',
                     'complemento',
                     'bairro',
                     'anotacoes',
                     )

admin.site.register(Cliente, ClienteAdmin)
