from django.contrib import admin

# Register your models here.
from .models import *
class Ozellestir(admin.ModelAdmin):
    search_fields = ('baslik',)
    

admin.site.register(Urunler_Metal,Ozellestir)
admin.site.register(Urunler_Metal_degil,Ozellestir)