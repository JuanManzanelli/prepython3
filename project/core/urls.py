from django.urls import path


app_name = "Core"

from . import views 

urlpatterns = [
    path("", views.home,name="home"),
]
