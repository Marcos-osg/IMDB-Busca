from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('filmes/',views.busca_filmes, name='filmes'),
]