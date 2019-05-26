from django.template.loader import render_to_string
from django.http import HttpResponse

from lifes.models import Photo, Profession, People


def show_main_page(request):

    people = People.objects.order_by('id')[:3]

    result = render_to_string('index.html', {
        'lifes': people,
    })

    return HttpResponse(result)