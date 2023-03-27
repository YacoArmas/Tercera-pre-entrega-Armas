from django.urls import path
from nouvelle_vague.views import *


urlpatterns = [
    path("", index, name="index"),
    path("guardar_user/", guardar_user, name="guardar_user"),
    path("guardar_movie/", guardar_movie, name="guardar_movie"),
    path("guardar_rental/", guardar_rental, name="guardar_rental"),
    path("buscar_year/", buscar_year, name="buscar_year"),
]
