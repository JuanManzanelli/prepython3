from django.urls import path

app_name = "region"

from . import views 

urlpatterns = [
    path("", views.home, name="home"),
]
