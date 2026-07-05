from django.shortcuts import render
from .models import *


def index_view(request):
    return render(request, 'portfolio/desenvolvedor.html')

def faculdade_view(request):
    return render(request, 'portfolio/faculdade.html')

def tfcs_view(request):
    context = {
        'tfcs': TFC.objects.all()
    }
    return render(request, 'portfolio/tfc.html', context)
