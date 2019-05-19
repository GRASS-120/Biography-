from django.contrib import admin

# Register your models here.

from lifes.models import Photo

from lifes.models import People

from lifes.models import Profession

admin.site.register(Photo)

admin.site.register(Profession)

admin.site.register(People)