from django.contrib import admin

# Register your models here.
from locadora.locadora_app.models import Filme


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ['id', 'capa', 'titulo', 'ano', 'diretor', 'sinopse', 'disponivel']
