from django.urls import path
from . import views

app_name = "inicio"

urlpatterns = [
    path('inicioo', views.list_producto, name="list_inicio"),
    path('crearpc', views.crear, name="crear_pc"),

]

