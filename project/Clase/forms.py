from django import forms        
from . import models

class ClaseCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ClaseCategoria    
        fields = "__all__"