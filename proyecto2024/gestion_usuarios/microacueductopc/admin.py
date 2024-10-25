from django.contrib import admin
from .models import Usuario, Vivienda, Cuota, Pago, Morosidad, Informe

admin.site.register(Usuario)
admin.site.register(Vivienda)
admin.site.register(Cuota)
admin.site.register(Pago)
admin.site.register(Morosidad)
admin.site.register(Informe)
