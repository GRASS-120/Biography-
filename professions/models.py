from django.db import models

# Create your models here.

class Profession (models.Model):
    profession = models.CharField(max_length=1000)

    discovery = models.TextField(max_length=10000)
    status = models.CharField(max_length=1000)