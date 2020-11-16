from django.contrib import admin
from .models import *

# Register your models here.
class registro1Admin(admin.ModelAdmin):
    list_display = ('nombre','apellido','rut','comuna','email','nombre_usario')
    fields=[('nombre','apellido','rut'),'comuna','email','nombre_usario']

#admin.site.register(registro1)