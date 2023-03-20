from django.urls import path
from nouvelle_vague.views import home, index


urlpatterns = [
    path("home/", home),
    path("index/", index),
]
