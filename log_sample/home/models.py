from django.db import models

# Create your models here.
class AddMovie(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=4)
    img = models.CharField(max_length=2000)
