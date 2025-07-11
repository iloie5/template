from django.db import models

# Create your models here.


class Reader(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)


