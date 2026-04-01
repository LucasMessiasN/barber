from django.contrib import admin
from .models import Cliente, Barbeiro, Atendimento

admin.site.register(Cliente)
admin.site.register(Barbeiro)
admin.site.register(Atendimento)