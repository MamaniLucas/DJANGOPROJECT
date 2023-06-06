from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("B")

def sumar(request, num1, num2):
    var1=int(num1)
    var2=int(num2)
    result="Suma = %s"%(var1+var2)
    return HttpResponse(result)

def resta(request, num1, num2):
    var1=int(num1)
    var2=int(num2)
    result="Resta = %s"%(var1-var2)
    return HttpResponse(result)


def multiplicacion(request, num1, num2):
    var1 = int(num1)
    var2 = int(num2)
    result = "Producto = %s" % (var1*var2)
    return HttpResponse(result)


def dividir(request, num1, num2):
    var1 = int(num1)
    var2 = int(num2)
    result = "Division = %s" % (var1/var2)
    return HttpResponse(result)


# Create your views here.
