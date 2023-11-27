from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'reserva'

router = routers.DefaultRouter()
router.register('reserva', views.ReservaViewSet, basename='reserva')

urlpatterns = [
    path('', include(router.urls) )
]