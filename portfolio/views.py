from django.shortcuts import render
from .models import Proyecto

def index(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'portfolio/index.html', {'proyectos': proyectos})