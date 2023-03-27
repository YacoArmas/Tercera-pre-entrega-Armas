from django.db import models


# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=99)
    year = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.year})"


class Users(models.Model):
    username = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return f"{self.username}"


class Rental(models.Model):
    movie = models.CharField(max_length=99)
    days = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.movie} - {self.days}"
