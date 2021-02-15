from django.shortcuts import render, HttpResponse, redirect

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
    return render(request, 'saludo.html')

def index(request):
    return render(request, 'index.html')

def rango(request,a,b):

    if a > b:
        return redirect('rango', a=b, b=a)
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



