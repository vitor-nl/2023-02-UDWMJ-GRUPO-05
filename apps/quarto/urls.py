from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'quarto'

router = routers.DefaultRouter()
router.register('quarto', views.QuartoViewSet, basename='quarto')

urlpatterns = [
    path('', include(router.urls) )
]