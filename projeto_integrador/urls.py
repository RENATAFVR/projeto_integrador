from django.contrib import admin
from django.urls import path
from app_PI import views

urlpatterns = [
    #url da pagina inicial (link)
    path('',views.home,name='home'), 
]

