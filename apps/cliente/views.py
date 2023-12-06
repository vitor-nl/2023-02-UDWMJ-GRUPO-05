from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from rest_framework import viewsets
from .serializer import ClienteSerializer
from .forms import ClienteForm
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

def add_cliente(request):
    template_name = 'cliente/add_cliente.html'
    context = {}
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('cliente:list_cliente')
    form = ClienteForm()
    context['form'] = form
    return render(request, template_name, context)

def list_cliente(request):
    template_name = 'cliente/list_cliente.html'
    cliente = Cliente.objects.filter()
    context = {
        'Cliente': cliente
    }
    return render(request, template_name, context)

def edit_cliente(request, id_cliente):
    template_name = 'cliente/add_cliente.html'
    context ={}
    cliente = get_object_or_404(Cliente, id=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=Cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente:list_cliente')
    form = ClienteForm(instance=cliente)
    context['form'] = form
    return render(request, template_name, context)

def delete_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect('cliente:list_cliente')