from django.shortcuts import render
from django.http import HttpResponse
from nouvelle_vague.models import *
from nouvelle_vague.forms import *


# Create your views here.
def index(request):
    return render(request, "nouvelle_vague/index.html")


def movies(request):
    return render(request, "nouvelle_vague/movies.html")


def profile(request):
    return render(request, "nouvelle_vague/profile.html")


def about(request):
    return render(request, "nouvelle_vague/about.html")


def guardar_rental(request):
    if request.method == "POST":
        miFormulario = AgregarRentalForm(
            request.POST
        )  # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(f"/n{informacion}/n")
            rental = Rental(movie=informacion["movie"], days=informacion["days"])
            rental.save()
            return render(request, "nouvelle_vague/index.html")
    else:
        miFormulario = AgregarRentalForm()

    return render(
        request, "nouvelle_vague/guardar_rental.html", {"miFormulario": miFormulario}
    )


def guardar_movie(request):
    if request.method == "POST":
        miFormulario = AgregarMovieForm(
            request.POST
        )  # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(f"/n{informacion}/n")
            movie = Movies(name=informacion["name"], year=informacion["year"])
            movie.save()
            return render(request, "nouvelle_vague/index.html")
    else:
        miFormulario = AgregarMovieForm()

    return render(
        request, "nouvelle_vague/guardar_form.html", {"miFormulario": miFormulario}
    )


def guardar_user(request):
    if request.method == "POST":
        miFormulario = AgregarUserForm(
            request.POST
        )  # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(f"/n{informacion}/n")
            user = Users(username=informacion["username"], email=informacion["email"])
            user.save()
            return render(request, "nouvelle_vague/index.html")
    else:
        miFormulario = AgregarUserForm()

    return render(
        request, "nouvelle_vague/guardar_user.html", {"miFormulario": miFormulario}
    )


def buscar_year(request):
    if request.method == "POST":
        miFormulario = BuscarYearForm(
            request.POST
        )  # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            years = Movies.objects.filter(id=informacion["year"])

            ## print(f"/n{informacion[years]}/n")
            return render(request, "nouvelle_vague/buscar_year.html", {"data": [years]})
    else:
        miFormulario = BuscarYearForm()

    return render(
        request, "nouvelle_vague/buscar_year.html", {"miFormulario": miFormulario}
    )
