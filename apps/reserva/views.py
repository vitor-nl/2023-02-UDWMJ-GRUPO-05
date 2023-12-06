from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from rest_framework import viewsets
from .serializer import ReservaSerializer
from .forms import ReservaForm

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

def add_reserva(request):
    template_name = 'reserva/add_reserva.html'
    context = {}
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('reserva:list_reserva')
    form = ReservaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_reserva(request):
    template_name = 'reserva/list_reserva.html'
    reserva = Reserva.objects.filter()
    context = {
        'Reserva': reserva
    }
    return render(request, template_name, context)

def edit_reserva(request, id_reserva):
    template_name = 'reserva/add_reserva.html'
    context ={}
    reserva = get_object_or_404(Reserva, id=id_reserva)
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES,  instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva:list_reserva')
    form = ReservaForm(instance=reserva)
    context['form'] = form
    return render(request, template_name, context)

def delete_reserva(request, id_reserva):
    reserva = Reserva.objects.get(id=id_reserva)
    reserva.delete()
    return redirect('reserva:list_reserva')