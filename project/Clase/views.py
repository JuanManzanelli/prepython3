from django.shortcuts import render

from . import models

def home(request):
    consulta_comision = models.Comision.objects.all()
    context = {"estudiantes": consulta_comision} 
    return render(request, "Clase/index.html", context)