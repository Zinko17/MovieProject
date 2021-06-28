from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'score', 'year', 'url']

admin.site.register(Movie,MovieAdmin)