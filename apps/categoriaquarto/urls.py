from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categoriaquarto'

urlpatterns = [
    path('', views.list_categoriaquarto, name='list_categoriaquarto'),
    path('adicionar/', views.add_categoriaquarto, name='add_categoriaquarto'),
    path('editar/<int:id_categoriaquarto>/', views.edit_categoriaquarto, name='edit_categoriaquarto'),
    path('excluir/<int:id_categoriaquarto>/', views.delete_categoriaquarto, name='delete_categoriaquarto'),
]