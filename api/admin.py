from django.contrib import admin

# Register your models here.
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('body', 'created', 'updated')


admin.site.register(Note, NoteAdmin)
