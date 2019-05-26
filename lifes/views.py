from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template.loader import render_to_string

from lifes.models import People
from professions.models import Profession


def show_life_detail (request, people_id):

    people = People.objects.get(id=people_id)
    result = render_to_string('index-2.html', {
        'people': people,
    })

    return HttpResponse(result)

