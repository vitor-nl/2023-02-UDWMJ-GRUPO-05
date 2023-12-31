from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoriaquarto
from rest_framework import viewsets
from .serializer import CategoriaquartoSerializer
from .forms import CategoriaquartoForm

# Create your views here.

class CategoriaquartoViewSet(viewsets.ModelViewSet):
    queryset = Categoriaquarto.objects.all()
    serializer_class = CategoriaquartoSerializer

def add_categoriaquarto(request):
    template_name = 'categoriaquarto/add_categoriaquarto.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaquartoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('categoriaquarto:list_categoriaquarto')
    form = CategoriaquartoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_categoriaquarto(request):
    template_name = 'categoriaquarto/list_categoriaquarto.html'
    categoriaquarto = Categoriaquarto.objects.filter()
    context = {
        'Categoriaquarto': categoriaquarto
    }
    return render(request, template_name, context)

def edit_categoriaquarto(request, id_categoriaquarto):
    template_name = 'categoriaquarto/add_categoriaquarto.html'
    context ={}
    categoriaquarto = get_object_or_404(Categoriaquarto, id=id_categoriaquarto)
    if request.method == 'POST':
        form = CategoriaquartoForm(request.POST, instance=categoriaquarto)
        if form.is_valid():
            form.save()
            return redirect('categoriaquarto:list_categoriaquarto')
    form = CategoriaquartoForm(instance=categoriaquarto)
    context['form'] = form
    return render(request, template_name, context)

def delete_categoriaquarto(request, id_categoriaquarto):
    categoriaquarto = Categoriaquarto.objects.get(id=id_categoriaquarto)
    categoriaquarto.delete()
    return redirect('categoriaquarto:list_categoriaquarto')
