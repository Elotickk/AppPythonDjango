from django.urls import path
from app_empresa import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listado/', views.listado, name='listado'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
]