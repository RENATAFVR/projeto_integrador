from django.contrib import admin
from django.urls import path
from app_PI import views

urlpatterns = [
    #url da pagina inicial (link)
    path('',views.home,name='home'), 
    path('usuario/cadastro',views.cadastrar_usuario,name='cadastro-usuario'), 
    path('usuario/login/', views.login_usuario, name='login'),
    path('usuario/logout/', views.logout_usuario, name='logout'),
]

