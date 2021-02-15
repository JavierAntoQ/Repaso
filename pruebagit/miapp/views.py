from django.shortcuts import render, HttpResponse

# Create your views here.
layout = """
    <h1>Proyecto WEB LP3 || Quispe Javier </h1>
    <hr/>
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
    <hr/>
    """ 
 
def saludo(request):
    mensaje = """
        <h1>BIENVENIDOS A LA UNTELS </h1>
        <h2>Facultad de Ingenieria </h2>
        <h3>EP Ingenieria de Sistemas </h3>
        <h4>LP III - JAVIER QUISPE </h4>
            """
    return HttpResponse(layout + mensaje)

def index(request):
    mensaje = """
        <h1>Inicio</h1>
        """
    return HttpResponse(layout + mensaje)

def rango(request,a,b):

    resultado = f"""
        <h1> Rango con parametros </h1>
        <h2> Numero de [{a} , {b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1

    resultado += "</ul>"
    return HttpResponse(layout + resultado)



