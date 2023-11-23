from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'servicoadicional'

router = routers.DefaultRouter()
router.register('servicoadicional', views.ServicoadicionalViewSet, basename='servicoadicional')

urlpatterns = [
    path('', include(router.urls) )
]