from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'quarto'

router = routers.DefaultRouter()
router.register('quarto', views.QuartoViewSet, basename='quarto')

urlpatterns = [
    path('', views.list_quarto, name='list_quarto'),
    path('adicionar/', views.add_quarto, name='add_quarto'),
    path('editar/<int:id_quarto>/', views.edit_quarto, name='edit_quarto'),
    path('excluir/<int:id_quarto>/', views.delete_quarto, name='delete_quarto'),
]