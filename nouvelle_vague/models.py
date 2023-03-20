from django.db import models


# Create your models here.
class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=99)


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=16)
    email = models.EmailField()


class Rental(models.Model):
    rental_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=10)
    overdue_flag = models.BooleanField()
