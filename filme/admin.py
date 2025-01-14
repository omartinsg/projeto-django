from django.contrib import admin
from .models import Filme, Episodio, Usuario
from  django.contrib.auth.admin import UserAdmin

# so existe por que a gente quer que no admin apareça o campo filmes vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Historico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)
# Register your models here.

admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario,UserAdmin)