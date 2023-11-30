from django.shortcuts import render, get_object_or_404, redirect

from rest_framework import viewsets
from quarto.models import Quarto
from quarto.serializer import QuartoSerializer
from quarto.forms import QuartoForm

class QuartoViewSet(viewsets.ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer

def add_quarto(request):
    template_name = 'quarto/add_quarto.html'
    context = {}
    if request.method == 'POST':
        form = QuartoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('quarto:list_quarto')
    form = QuartoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_quarto(request):
    template_name = 'quarto/list_quarto.html'
    quarto = Quarto.objects.filter()
    context = {
        'quarto': Quarto
    }
    return render(request, template_name, context)

def edit_quarto(request, id_quarto):
    template_name = 'quarto/add_quarto.html'
    context ={}
    quarto = get_object_or_404(Quarto, id=id_quarto)
    if request.method == 'POST':
        form = QuartoForm(request.POST, instance=quarto)
        if form.is_valid():
            form.save()
            return redirect('quarto:list_quarto')
    form = QuartoForm(instance=quarto)
    context['form'] = form
    return render(request, template_name, context)

def delete_quarto(request, id_quarto):
    quarto = Quarto.objects.get(id=id_quarto)
    quarto.delete()
    return redirect('quarto:list_quarto')


