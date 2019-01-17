from django.contrib import admin
from .models import Cadastro, Estado, Cidade


admin.site.register(Cadastro)
admin.site.register(Estado)
admin.site.register(Cidade)