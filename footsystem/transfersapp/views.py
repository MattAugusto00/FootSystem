from django.shortcuts import render
from .models import Clube

def home(request):
    return render(request, 'clubes/home.html')

def clubes(request):
    novo_clube = Clube()
    novo_clube.nome = request.POST.get('nome')
    novo_clube.estado = request.POST.get('estado')
    novo_clube.save()

    clubes = {
        'clubes': Clube.objects.all()
    }

    return render(request, 'clubes/clubes.html', clubes)