from django.urls import path

from . import views

urlpatterns = [
    path('lifes/<int:people_id>/',
        views.show_life_detail),
]