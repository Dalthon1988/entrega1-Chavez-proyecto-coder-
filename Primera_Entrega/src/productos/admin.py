from django.contrib import admin
from productos.models import Vegetales,Perecederos,NoPerecederos

# Register your models here.
admin.site.register(Vegetales)
admin.site.register(Perecederos)
admin.site.register(NoPerecederos)
