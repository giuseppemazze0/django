from django.shortcuts import render
from .models import *


def index_view(request):
    context = {
        'tfcs': TFC.objects.all()
    }
    return render(request, 'portfolio/index.html', context)
