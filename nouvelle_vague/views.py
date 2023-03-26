from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "nouvelle_vague/index.html")


def movies(request):
    return render(request, "nouvelle_vague/movies.html")


def profile(request):
    return render(request, "nouvelle_vague/profile.html")


def about(request):
    return render(request, "nouvelle_vague/about.html")
