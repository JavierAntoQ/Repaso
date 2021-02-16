from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Reseña

# Create your views here.
layout = """
    <h1>
        <ul>
            <li>
                <a href="/inicio"> INICIO </a> 
            </li>
            <li> 
                <a href="/saludo"> MENSAJE DE SALUDO </a>
            </li>
            <li> 
                <a href="/rango/10/20"> RANGO </a> 
             </li>
        </ul>
    </h1>
    """

def saludo(request):
    return render(request, 'saludo.html',{
        'titulo':'Saludo',
        'nombre':'Quispe Calixto, Javier'
    })

def index(request):

    estudiantes = [
        'SERGIO DANIEL VITE COCHACHIN',
        'ANTHONY GERARDO BENDEZU SANTISTEBAN',
        'CRISTIAN ALEXIS CHIPANA HUAMAN',
        'CARLOS GUSTAVO OYOLA SAAVEDRA',
        'GERARDO MANUEL CASTILLO TORDOYA'
    ]

    return render(request, 'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto web con Django',
        'estudiantes': estudiantes
    })

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a, b+1)

    return render(request, 'rango.html',{
        'titulo':'Rango (Desde el view)',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })

def crear_reseña(request, titulo, contenido, publicado):
    reseña = Reseña(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    reseña.save()
    return HttpResponse(f"Reseña Creada: {reseña.titulo} - {reseña.contenido}")





