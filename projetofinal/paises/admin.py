from django.contrib import admin
from .models import Pais, Idioma

# Register your models here.
class PaisAdmin(admin.ModelAdmin):
    search_fields = ['nome_oficial']

admin.site.register(Pais, PaisAdmin)
admin.site.register(Idioma)
