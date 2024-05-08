from django.shortcuts import render, redirect

from . import forms, models

def home(request):
    consulta_region = models.RegionCategoria.objects.all()
    context = {"regiones": consulta_region} 
    return render(request, "region/index.html", context)


def regioncategoria_create(request):
    if request.method == "POST":
          form = forms.RegionCategoriaForm(request.POST)
          if form.is_valid():
               form.save() 
               return redirect("region:home")   
    else: 
        form= forms.RegionCategoriaForm()
    return render(request, "region/regioncategoria_create.html", context={"form": form})