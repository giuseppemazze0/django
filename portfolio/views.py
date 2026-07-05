from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index_view(request):
    return render(request, 'portfolio/desenvolvedor.html')



def faculdade_view(request):
    return render(request, 'portfolio/faculdade.html')



def tfcs_view(request):
    context = { 'tfcs': TFC.objects.all() }
    return render(request, 'portfolio/tfc.html', context)



def projetos_view(request):
    context = { 'projetos': Projeto.objects.all() }
    return render(request, 'portfolio/projetos.html', context)

def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    context = { 'form': form }
    return render(request, 'portfolio/novo_projeto.html', context)

def editar_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)
    context = { 'projeto': projeto, 'form': form }
    return render(request, 'portfolio/editar_projeto.html', context)

def apagar_projeto_view(request, projeto_id):
    Projeto.objects.get(id=projeto_id).delete()
    return redirect('projetos')




def tecnologias_view(request):
    context = {'tecnologias': Tecnologia.objects.all()}
    return render(request, 'portfolio/tecnologias.html', context)

def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    context = {'form': form}
    return render(request, 'portfolio/nova_tecnologia.html', context)

def editar_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)

    if request.POST:
        form = TecnologiaForm(request.POST or None, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    context = {
        'tecnologia': tecnologia,
        'form': form
    }
    return render(request, 'portfolio/editar_tecnologia.html', context)

def apagar_tecnologia_view(request, tecnologia_id):
    Tecnologia.objects.get(id=tecnologia_id).delete()
    return redirect('tecnologias')




def competencias_view(request):
    context = {'competencias': Competencia.objects.all()}
    return render(request, 'portfolio/competencias.html', context)

def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    context = {'form': form}
    return render(request, 'portfolio/nova_competencia.html', context)

def editar_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)

    if request.POST:
        form = CompetenciaForm(request.POST or None, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)

    context = {
        'competencia': competencia,
        'form': form
    }
    return render(request, 'portfolio/editar_competencia.html', context)

def apagar_competencia_view(request, competencia_id):
    Competencia.objects.get(id=competencia_id).delete()
    return redirect('competencias')




def formacoes_view(request):
    context = {'formacoes': Formacao.objects.all()}
    return render(request, 'portfolio/formacoes.html', context)

def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    context = {'form': form}
    return render(request, 'portfolio/nova_formacao.html', context)

def editar_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)

    if request.POST:
        form = FormacaoForm(request.POST or None, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)

    context = {
        'formacao': formacao,
        'form': form
    }
    return render(request, 'portfolio/editar_formacao.html', context)

def apagar_formacao_view(request, formacao_id):
    Formacao.objects.get(id=formacao_id).delete()
    return redirect('formacoes')