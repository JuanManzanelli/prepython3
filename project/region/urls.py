from django.urls import path
from . import views 

app_name = "region"


urlpatterns = [
    path("", views.home, name="home"),
    path("regioncategoria/create/", views.regioncategoria_create, name="regioncategoria_create"),
]
