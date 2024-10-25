# acueducto/urls.py

from django.urls import path
from .views import ViviendaList  # Asegúrate de importar tus vistas
from .views import ViviendaList, ViviendaDetail  # Asegúrate de importar tus vistas


urlpatterns = [
    path('viviendas/', ViviendaList.as_view(), name='vivienda-list'),
    # Aquí puedes agregar más rutas para otras vistas de la app
    path('viviendas/<int:pk>/', ViviendaDetail.as_view(), name='vivienda-detail'),  # Nueva ruta para una vivienda específica
]
