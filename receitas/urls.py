from unicodedata import name
from django.urls import path

from . import views

#cria arq .py para fazer sincronia com o Views ( as urls do site )

urlpatterns = [
    path('', views.index, name ='index'),
    path('<int:receita_id>', views.receita, name = 'receita'),
    path('buscar', views.buscar, name='buscar')
]