# reservas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_reservas, name='lista_reservas'),
    path('nova/', views.nova_reserva, name='nova_reserva'),
]
