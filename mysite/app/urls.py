from django.urls import path
#app.views
from app.views import sumar,multiplicacion, resta,  dividir 
from . import views 



urlpatterns =[
    path('', views.index, name='index'),
    path('sumar/<int:num1>/<int:num2>', sumar),
    path('restar/<int:num1>/<int:num2>', resta),
    path('multiplicar/<int:num1>/<int:num2>', multiplicacion),
    path('dividir/<int:num1>/<int:num2>', dividir)

    
]