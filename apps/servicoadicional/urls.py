from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'servicoadicional'

router = routers.DefaultRouter()
router.register('servicoadicional', views.ServicoadicionalViewSet, basename='servicoadicional')

urlpatterns = [
    path('', views.list_servicoadicional, name='list_servicoadicional'),
    path('adicionar/', views.add_servicoadicional, name='add_servicoadicional'),
    path('editar/<int:id_servicoadicional>/', views.edit_servicoadicional, name='edit_servicoadicional'),
    path('excluir/<int:id_servicoadicional>/', views.delete_servicoadicional, name='delete_servicoadicional'),
]