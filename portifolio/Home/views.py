from django.shortcuts import render
from .models import Projects, Servico, Pergunta, Tecnologia
from django.http import HttpRequest
# Create your views here.

def home(request: HttpRequest):
    projetos =  Projects.objects.all()
    serviços = Servico.objects.all()
    perguntas = Pergunta.objects.all()
    tecnologias = Tecnologia.objects.all()

    context = {
        'projetos': projetos,
        'servicos': serviços,
        'perguntas': perguntas,
        'tecnologias': tecnologias,
    }

    return render(request, 'Home/home.html', context)


