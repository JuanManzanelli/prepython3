from django.shortcuts import render

from . import models

def home(request):
    consulta_region = models.RegionCategoria.objects.all()
    context = {"regiones": consulta_region} 
    return render(request, "region/index.html", context)

def regioncategoria_create(request):
    return render(request, "region/regioncategoria_create.html")