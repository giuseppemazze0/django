from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *



def gestor_portfolio(user):
    return user.is_authenticated and user.groups.filter(
        name='gestor-portfolio'
    ).exists()



def index_view(request):
    return render(request, 'portfolio/desenvolvedor.html')



def faculdade_view(request):
    return render(request, 'portfolio/faculdade.html')



def tfcs_view(request):
    tfcs = TFC.objects.all()

    for tfc in tfcs:
        tfc.lista_palavras_chave = [
            palavra.strip()
            for palavra in tfc.palavras_chave.split(";")
            if palavra.strip()
        ]

    context = {"tfcs": tfcs}

    return render(request, "portfolio/tfc.html", context)



def sobre_aplicacao_view(request):
    return render(request, 'portfolio/sobre_aplicacao.html')



def projetos_view(request):
    return render(request, 'portfolio/projetos.html', {
        'projetos': Projeto.objects.all(),
        'is_gestor': gestor_portfolio(request.user)
    })

@login_required
@user_passes_test(gestor_portfolio)
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    context = { 'form': form }
    return render(request, 'portfolio/novo_projeto.html', context)

@login_required
@user_passes_test(gestor_portfolio)
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

@login_required
@user_passes_test(gestor_portfolio)
def apagar_projeto_view(request, projeto_id):
    Projeto.objects.get(id=projeto_id).delete()
    return redirect('projetos')




def tecnologias_view(request):
    return render(request, 'portfolio/tecnologias.html', {
        'tecnologias': Tecnologia.objects.all(),
        'is_gestor': gestor_portfolio(request.user)
    })

@login_required
@user_passes_test(gestor_portfolio)
def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    context = {'form': form}
    return render(request, 'portfolio/nova_tecnologia.html', context)

@login_required
@user_passes_test(gestor_portfolio)
def editar_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)

    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)
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

@login_required
@user_passes_test(gestor_portfolio)
def apagar_tecnologia_view(request, tecnologia_id):
    Tecnologia.objects.get(id=tecnologia_id).delete()
    return redirect('tecnologias')




def competencias_view(request):
    return render(request, 'portfolio/competencias.html', {
        'competencias': Competencia.objects.all(),
        'is_gestor': gestor_portfolio(request.user)
    })

@login_required
@user_passes_test(gestor_portfolio)
def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    context = {'form': form}
    return render(request, 'portfolio/nova_competencia.html', context)

@login_required
@user_passes_test(gestor_portfolio)
def editar_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)

    if request.POST:
        form = CompetenciaForm(request.POST or None, request.FILES, instance=competencia)
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

@login_required
@user_passes_test(gestor_portfolio)
def apagar_competencia_view(request, competencia_id):
    Competencia.objects.get(id=competencia_id).delete()
    return redirect('competencias')




def formacoes_view(request):
    return render(request, 'portfolio/formacoes.html', {
        'formacoes': Formacao.objects.all(),
        'is_gestor': gestor_portfolio(request.user)
    })

@login_required
@user_passes_test(gestor_portfolio)
def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    context = {'form': form}
    return render(request, 'portfolio/nova_formacao.html', context)

@login_required
@user_passes_test(gestor_portfolio)
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

@login_required
@user_passes_test(gestor_portfolio)
def apagar_formacao_view(request, formacao_id):
    Formacao.objects.get(id=formacao_id).delete()
    return redirect('formacoes')