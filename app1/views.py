from django.shortcuts import render
from app1.models import Profession
def index_page(regest):
    data = {
        'profession': Profession.objects.get(id=1)
    }
    return render(regest, 'index.html', context=data)
def home_page(regest):
    return render(regest, 'home.html')
def demanda_page(reqest):
    return render(reqest,'demanda.html')
def geografia_page(regest):
    return render(regest, 'geografia.html')
def habilidades_page(regest):
    return render(regest,'habilidades.html')
def vacantes_page(regest):
    return render(regest, 'vacantes.html')