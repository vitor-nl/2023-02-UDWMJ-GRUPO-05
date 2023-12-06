from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'reserva'

router = routers.DefaultRouter()
router.register('reserva', views.ReservaViewSet, basename='reserva')

urlpatterns = [
    path('', views.list_reserva, name='list_reserva'),
    path('adicionar/', views.add_reserva, name='add_reserva'),
    path('editar/<int:id_reserva>/', views.edit_reserva, name='edit_reserva'),
    path('excluir/<int:id_reserva>/', views.delete_reserva, name='delete_reserva'),
]