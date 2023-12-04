from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cliente'

router = routers.DefaultRouter()
router.register('cliente', views.ClienteViewSet, basename='cliente')

urlpatterns = [
    path('', views.list_cliente, name='list_cliente'),
    path('adicionar/', views.add_cliente, name='add_cliente'),
    path('editar/<int:id_cliente>/', views.edit_cliente, name='edit_cliente'),
    path('excluir/<int:id_cliente>/', views.delete_cliente, name='delete_cliente'),
]