from django.contrib import admin
from cliente.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    raw_id_fields = ('cidade',)
    autocomplete_lookup_fields = {
        'fk': ['cidade'],
    }
    list_display = (
                    'nome',
                    'sobrenome',
                    'email',
                    'telefone',
                    'endereco',
                    )

admin.site.register(Cliente, ClienteAdmin)
