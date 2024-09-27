from django.contrib import admin
from .models import Rubro, Cliente

class RubroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rubros', 'email', 'imagen', 'creado', 'editado')
    list_filter = ('rubros', 'creado')

admin.site.register(Rubro, RubroAdmin)
admin.site.register(Cliente, ClienteAdmin)
