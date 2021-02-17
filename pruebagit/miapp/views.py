from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Reseña, Autor

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

def buscar_reseña(request, id):
    try:
        reseña = Reseña.objects.get(pk=id)
        resultado = f"Reseña encontrada: <br> {reseña.id} - {reseña.titulo}"
    except:
        resultado = "<h1> Reseña no encontrada </h1>"
    return HttpResponse(resultado)

def editar_reseña(request, id):
    reseña = Reseña.objects.get(pk=id)
    reseña.titulo = "Enseñanza online en la UNTELS"
    reseña.contenido = "Aula virtual, Google Meet, Portal academico"
    reseña.publicado = False

    reseña.save()
    return HttpResponse(f"Reseña Editado: {reseña.titulo} - {reseña.contenido}")

def listar_reseñas(request):
    reseñas = Reseña.objects.all
    return render(request, 'listar_reseñas.html',{
        'reseñas' : reseñas,
        'titulo' : 'LISTADO DE RESEÑAS'
    })

def eliminar_reseña(request, id):
    reseña = Reseña.objects.get(pk=id)
    reseña.delete()
    return redirect('listar_reseñas')

def save_reseña(request):
    if request.method == 'POST':
        titulo =request.POST['titulo']
        contenido = request.POST['contenido']
        publicado = request.POST['publicado']

        reseña = Reseña(
            titulo = titulo,
            contenido = contenido, 
            publicado = publicado,
    )
        reseña.save()
        return HttpResponse(f"Reseña Creada: {reseña.titulo} - {reseña.contenido}")
    else:
        return HttpResponse("<h2> No se ha podido registar la reseña </h2>")
def create_reseña(request):
    return render(request, 'create_reseña.html')


def crear_autor(request, nombre, apellido, sexo, fecha_nacimiento, pais):
    autor = Autor(
        nombre = nombre,
        apellido = apellido, 
        sexo = sexo,
        fecha_nacimiento = fecha_nacimiento,
        pais = pais,
    )
    autor.save()
    return HttpResponse(f"Autor Creado: {autor.apellido}, {autor.nombre} - ({autor.pais})")

def buscar_autor(request, id):
    try:
        autor = Autor.objects.get(pk=id)
        resultado = f"Autor encontrada: <br> {autor.id} - {autor.apellido}"
    except:
        resultado = "<h1> Autor no encontrado </h1>"
    return HttpResponse(resultado)

def editar_autor(request, id):
    autor = Autor.objects.get(pk=id)
    autor.nombre = "German"
    autor.apellido = "Perrez"
    autor.sexo = "Masculino"
    autor.fecha_nacimiento = "12/05/1999"
    autor.pais = "Peru"

    autor.save()
    return HttpResponse(f"Autor Editado: {autor.titulo} - {autor.contenido}")

def listar_autores(request):
    autores = Autor.objects.all
    return render(request, 'listar_autores.html',{
        'autores' : autores,
        'titulo' : 'LISTADO DE AUTORES'
    })

def eliminar_autor(request, id):
    autor = Autor.objects.get(pk=id)
    autor.delete()
    return redirect('listar_autores')

def save_autor(request):
    if request.method == 'POST':
        nombre =request.POST['nombre']
        apellido = request.POST['apellido']
        sexo = request.POST['sexo']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        pais = request.POST['pais']

        autor = Autor(
            nombre = nombre,
            apellido = apellido, 
            sexo = sexo,
            fecha_nacimiento = fecha_nacimiento,
            pais = pais,
    )
        autor.save()
        return HttpResponse(f"Autor Creado: {autor.apellido}, {autor.nombre} - ({autor.fecha_nacimiento})")
    else:
        return HttpResponse("<h2> No se ha podido registar a el autor </h2>")

def create_autor(request):
    return render(request, 'create_autor.html')

