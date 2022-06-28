from django.contrib import admin

# Register your models here.
from proyecto_cursoApp.models import Comentrio, Curso, Evento

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'info', 'fecha')

admin.site.register(Curso, CursoAdmin)

class EventoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'info', 'fecha')
    
admin.site.register(Evento, EventoAdmin)
  
class ComentarioAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'email', 'mensaje')

admin.site.register(Comentrio, ComentarioAdmin)

#user= admin - contraseña= 1234