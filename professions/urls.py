from django.urls import path

from . import views

urlpatterns = [
    path('professions/',
        views.show_profession_detail),
]