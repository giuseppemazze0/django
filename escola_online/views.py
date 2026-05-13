from django.shortcuts import render
from .models import Curso

cursos = Curso.objects.select_related('professor_responsavel').prefetch_related('alunos').all()
context = { 'cursos': cursos }



def cursos_view(request):
    return render(request, 'escola-online/cursos.html', context)



def curso_view(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'escola-online/curso.html', {'curso': curso})



def professores_view(request):
    return render(request, 'escola-online/professores.html', context)



def alunos_view(request):
    return render(request, 'escola-online/alunos.html', context)