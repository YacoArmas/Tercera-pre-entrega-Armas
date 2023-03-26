from django.urls import path
from nouvelle_vague.views import *


urlpatterns = [
    path("", index),
    path("movies/", movies),
    path("profile/", profile),
    path("about/", about),
]
