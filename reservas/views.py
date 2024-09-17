# reservas/views.py

from django.shortcuts import render, redirect
from .models import Reserva, Sala
from django.utils import timezone

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

def nova_reserva(request):
    if request.method == 'POST':
        sala_id = request.POST.get('sala_id')
        data_reserva = request.POST.get('data_reserva')
        sala = Sala.objects.get(id=sala_id)
        Reserva.objects.create(sala=sala, data_reserva=data_reserva)
        return redirect('lista_reservas')

    salas = Sala.objects.all()
    return render(request, 'reservas/nova_reserva.html', {'salas': salas})
