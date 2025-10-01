from django.contrib import admin
from .models import Vendedor

# Register your models here.
@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'rg','data_nascimento', 'sexo', 'criado_em', 'atualizado_em', 'ativo' )
    search_fields = ('nome', 'email',)

