from django.contrib import admin
from django.urls import path
from .views import PaisListView, PaisFormView, PaisDetailView, PaisDeleteView
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('listar/', PaisListView.as_view(), name='lista_pais'),
    path('forms/', PaisFormView.as_view(), name='form_pais'),
    path('detail/<int:pk>/', PaisDetailView.as_view(), name='detalhe_pais'),
    path('delete/<int:pk>/', PaisDeleteView.as_view(), name='deleta_pais'),
]
