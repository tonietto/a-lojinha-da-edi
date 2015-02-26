from django.contrib import admin
from blog.models import Post, Categoria


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}


class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
