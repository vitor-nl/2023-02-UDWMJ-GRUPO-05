from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicoadicional
from rest_framework import viewsets
from .serializer import ServicoadicionalSerializer
from .forms import ServicoadicionalForm

class ServicoadicionalViewSet(viewsets.ModelViewSet):
    queryset = Servicoadicional.objects.all()
    serializer_class = ServicoadicionalSerializer 

def add_servicoadicional(request):
    template_name = 'servicoadicional/add_servicoadicional.html'
    context = {}
    if request.method == 'POST':
        form = ServicoadicionalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('servicoadicional:list_servicoadicional')
    form = ServicoadicionalForm()
    context['form'] = form
    return render(request, template_name, context)

def list_servicoadicional(request):
    template_name = 'servicoadicional/list_servicoadicional.html'
    servicoadicional = Servicoadicional.objects.filter()
    context = {
        'Servicoadicional': servicoadicional
    }
    return render(request, template_name, context)

def edit_servicoadicional(request, id_servicoadicional):
    template_name = 'servicoadicional/add_servicoadicional.html'
    context ={}
    servicoadicional = get_object_or_404(Servicoadicional, id=id_servicoadicional)
    if request.method == 'POST':
        form = ServicoadicionalForm(request.POST, instance=servicoadicional)
        if form.is_valid():
            form.save()
            return redirect('servicoadicional:list_servicoadicional')
    form = ServicoadicionalForm(instance=servicoadicional)
    context['form'] = form
    return render(request, template_name, context)

def delete_servicoadicional(request, id_servicoadicional):
    servicoadicional = Servicoadicional.objects.get(id=id_servicoadicional)
    servicoadicional.delete()
    return redirect('servicoadicional:list_servicoadicional')