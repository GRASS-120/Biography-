from django.db import models

# Create your models here.
from professions.models import Profession


class Photo(models.Model):
    url = models.TextField(max_length=1000000)

class People(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    location = models.CharField(max_length=1000)
    photo = models.ForeignKey(
        to=Photo,
        related_name='people',
        on_delete=models.CASCADE,
    )
    profession = models.ForeignKey(
        to=Profession,
        related_name='people',
        on_delete = models.CASCADE,
    )

