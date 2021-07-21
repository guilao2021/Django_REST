from django.contrib import admin
from tabela_precos.models import Tratamento

class Tratamentos(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'valor']
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)

admin.site.register(Tratamento, Tratamentos)