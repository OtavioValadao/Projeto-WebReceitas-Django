from unicodedata import name
from django.urls import path
from . import views

#cria arq .py para fazer sincronia com o Views ( as urls do site )

urlpatterns = [
    path('cadastro', views.cadastro, name ='cadastro'),
    path('login', views.login, name ='login'),  
    path('logout', views.logout, name ='logout'),  
    path('dashboard', views.dashboard, name ='dashboard'),  
]