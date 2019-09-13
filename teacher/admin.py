from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Professor)


class WordAdmin(admin.ModelAdmin):
    list_display = ("word", "frequency", "relative_frequency")


admin.site.register(Word, WordAdmin)
