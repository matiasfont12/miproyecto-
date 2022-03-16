from django.urls import path
from .views import inicio, mi_plantilla, otra_vista, mi_plantilla

urlpatterns = [
    path("inicio/", inicio),
    path("plantilla/", mi_plantilla),
    path("",otra_vista)
]