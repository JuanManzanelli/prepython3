from django.urls import path

app_name = "Clase"

from . import views 

urlpatterns = [
    path("", views.home, name="home"),
]
