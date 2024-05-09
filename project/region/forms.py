from django import forms

from . import models

#class Regioncategoriaform(forms.Form):
#  nombre = forms.CharField()
#  zona = forms.CharField()

class RegionCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.RegionCategoria
        fields = ["nombre","zona"]