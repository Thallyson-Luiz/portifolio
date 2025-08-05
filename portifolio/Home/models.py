from typing import Iterable
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from utils.resizeImagem import redimensionar_imagem

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField(max_length=500, blank=True, null=True, default='')
    descricao = models.TextField(max_length=200)
    img = models.ImageField(upload_to='projects/imagens/%Y')
    icon = models.ImageField(upload_to='projects/icon/%Y')
    

    def save(self, *args, **kwargs) -> None:
        if not self.pk and Projects.objects.count() >= 3:
            raise ValidationError('O maximo de projetos permitidos é 2')
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def clean(self) -> None:
        if self.pk and Projects.objects.count() >= 3:
            raise ValidationError('O maximo de projetos permitidos é 2')
        return super().clean()
    
class Servico(models.Model):
    class Meta:
        verbose_name_plural = 'Servicos'

    title = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    imagem = models.ImageField(upload_to='servicos/%Y')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        retornar =  super().save(*args, **kwargs)
        imagem = self.imagem.path
        redimensionar_imagem(imagem, 400)
        return retornar
    
class Pergunta(models.Model):
    class Meta:
        verbose_name_plural = 'Perguntas'
        
    pergunta = models.CharField(max_length=200)
    resposta = models.TextField(max_length=2000)

    def __str__(self):
        return self.pergunta
    
class Tecnologia(models.Model):
    class Meta:
        verbose_name_plural = 'Tecnologias'
        
    title = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='tecnologias/%Y')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        retornar =  super().save(*args, **kwargs)
        imagem = self.imagem.path
        redimensionar_imagem(imagem, 800)
        return retornar



