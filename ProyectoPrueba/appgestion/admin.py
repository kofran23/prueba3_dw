from django.contrib import admin

# Register your models here.

from appgestion.models import Cliente,Casas,Compra

admin.site.register(Cliente)
admin.site.register(Casas)
admin.site.register(Compra)

