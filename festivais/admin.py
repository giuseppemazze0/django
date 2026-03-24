from django.contrib import admin
from .models import Genero, Banda, Festival


class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nome",)



class BandaAdmin(admin.ModelAdmin):
    list_display = ("nome", "genero")
    search_fields = ("nome", "genero__nome")
    list_filter = ("nome", "genero__nome")



class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nome",)



admin.site.register(Genero, GeneroAdmin)
admin.site.register(Banda, BandaAdmin)
admin.site.register(Festival, FestivalAdmin)