from django.contrib import admin
from .models import Receita


# Register your models here.

class ListandoRecietas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'ativa')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('ativa',)
    list_per_page = 10


admin.site.register(Receita, ListandoRecietas)
