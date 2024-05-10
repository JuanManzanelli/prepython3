from django.shortcuts import render, redirect
from . import forms, models

def home(request):
    consulta_clase = models.ClaseCategoria.objects.all()
    context = {"Clases": consulta_clase} 
    return render(request, "clase/index.html", context)


def clasecategoria_create(request):
    if request.method == "POST":    
         form = forms.ClaseCategoriaForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect("clase:home")
    else:
         form = forms.ClaseCategoriaForm()
    return render(request, "clase/clasecategoria_create.html", context={"form": form})

