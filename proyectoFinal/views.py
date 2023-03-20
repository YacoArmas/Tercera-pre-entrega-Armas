from django.http import HttpResponse
from django.template import Template, Context, loader


def saludo(request):
    return HttpResponse("hola mundo")


def probandoTemplate(request):
    plantilla = loader.get_template("template1.html")

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)
