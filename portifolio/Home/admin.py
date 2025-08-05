from django.contrib import admin
from django.http import HttpRequest
from . import models
# Register your models here.
@admin.register(models.Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    list_display_links = ('title',)

    def has_add_permission(self, request: HttpRequest) -> bool:
        if models.Projects.objects.count() >= 3:
            return False
        return super().has_add_permission(request)
    
@admin.register(models.Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('title', 'descricao')
    list_display_links = ('title',)

@admin.register(models.Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'resposta')
    list_display_links = ('pergunta',)

@admin.register(models.Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('title', 'imagem')
    list_display_links = ('title',)