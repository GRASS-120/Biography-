from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from professions.models import Profession


def show_profession_detail (request, profession_id):

    profession = Profession.objects.get(id=profession_id)
    result = render_to_string('index-3.html', {
        'profession': profession,
    })

    return HttpResponse(result)