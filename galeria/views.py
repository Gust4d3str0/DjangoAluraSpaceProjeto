from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse #Responder requisição
from galeria.models import Fotografia



def index(request):
    fotografias = Fotografia.objects.filter(publicada=True).order_by('-data_fotografia')
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})