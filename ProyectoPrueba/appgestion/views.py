from django.shortcuts import render
from django.http import HttpResponse
from appgestion.models import Casas

# Create your views here.
def busqueda_casas(request):
    return render(request,"busqueda_casas.html")

def formulario_ingreso(request):
    return render(request,"ingresar_casa.html")

def formulario_eliminar(request):
    return render(request,"eliminar_casa.html")

def index(request):
    return render(request, "index.html")       

def buscar(request):
    if request.GET["txt_casa"]:
        casa_recibida = request.GET["txt_casa"]
        casas=Casas.objects.filter(medidas__contains=casa_recibida)
        return render(request,"resultado_busqueda.html",{"casas":casas,"casa_consultada":casa_recibida})
    else:
       mensaje="debe ingresar una casa a buscar"
    return HttpResponse(mensaje)

def buscarPrecio(request):
    if request.GET["txt_precio"]:
        precio = request.GET["txt_precio"]
        casas=Casas.objects.filter(precio__gte=precio)
        return render(request,"resultado_precio.html",{"casas":casas,"precio_recibido":precio})
    else:
       mensaje="no existen casas con ese precio"
    return HttpResponse(mensaje)

def ingresar_casa(request):
    ciudad=request.GET["txt_ciudad"]
    medidas=request.GET["txt_medidas"]
    categoria=request.GET["txt_precio"]
    precio=request.GET["txt_precio"]
    if len(ciudad)>0 and len(medidas)>0 and len(categoria)>0 and len(precio)>0:
        cas=Casas(ciudad=ciudad,medidas=medidas,categoria=categoria,precio=precio)
        cas.save()
        mensaje="Casa Ingresada"
    else:
        mensaje="Casa no ingresado, faltan datos o hubo error en llenado"
        return HttpResponse(mensaje)

def eliminar_casa(request):
    if request.GET["txt_id"]: 
        id_recibido=request.GET["txt_id"]
        casa=Casas.objects.filter(categoria=id_recibido)        
        if casa:
            cas=Casas.objects.get(categoria=id_recibido)
            cas.delete()            
            mensaje="Casa eliminada"
        else:
            mensaje="Casa no eliminada no existe casa con esa categoria"
    else:
        mensaje="Debe ingresar una categoria"
    return HttpResponse(mensaje)        