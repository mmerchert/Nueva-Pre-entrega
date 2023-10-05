from django.urls import path
from .views import *

urlpatterns = [

    path("inicio/", inicio, name="Inicio"),
    path("gatos/", ver_gatos, name="VerGatos"),
    path("perros/", ver_perros, name="VerPerros"),
    path("peces/", ver_peces, name="VerPeces"),
    path("compraFormulario/", compraFormulario, name="FormularioCompra"),
    path("buscarCompra/", busquedaCompra, name="BuscarCompra"),
    path("resultados/", resultados, name="ResultadosBusqueda"),

]
