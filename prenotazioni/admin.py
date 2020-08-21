from django.contrib import admin
from .models import Clienti, Prenotazioni, Configurazione

# Register your models here.
class ClientiModelAdmin(admin.ModelAdmin):
    list_display = [ "nome","cognome","eta","indirizzo","telefono","livello","email","password"]
    search_fields = ["nome","cognome","eta","indirizzo","telefono","livello","email"]



class PrenotazioniModelAdmin(admin.ModelAdmin):
    list_display = [ "giorno","ora","cliente", "note"]
    search_fields = ["giorno","ora","cliente"]

class ConfigurazioneModelAdmin(admin.ModelAdmin):
    list_display = ["id", "orariuscitesettimanali", "giorniuscitesettimanali", "numeropartecipantiperturno"]
    search_fields = ["orariuscitesettimanali", "giorniuscitesettimanali", "numeropartecipantiperturno"]

admin.site.register(Clienti,ClientiModelAdmin)
admin.site.register(Configurazione,ConfigurazioneModelAdmin)
admin.site.register(Prenotazioni,PrenotazioniModelAdmin)