from django.urls import path
from . import views

urlpatterns = [
    path('', views.profesores_list, name='profesores_list'),
]