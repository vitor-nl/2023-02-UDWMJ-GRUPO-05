from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categoriaquarto'

router = routers.DefaultRouter()
router.register('categoriaquarto', views.CategoriaquartoViewSet, basename='categoriaquarto')

urlpatterns = [
    path('', include(router.urls) )
]