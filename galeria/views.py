from django.shortcuts import render
from django.http import HttpResponse #Responder requisição




def index(request):
    
    dados = {
   1: { "nome": "Nebulosa de Carina",
    "legenda": "webbtelecope.org / NASA / James Webb Space Telescope"},
   
   2: {"nome": "Galaxia NGC 1079", 
       "legenda": "ESA/Hubble & NASA, J. Lee and the PHANGS-HST Team"}
   }
    
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')