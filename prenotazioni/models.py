from django.db import models

# Create your models here.
class Clienti(models.Model):
        nome= models.CharField(max_length=50, default="")
        cognome = models.CharField(max_length=50, default="")
        eta= models.IntegerField(blank=True, null=True)
        indirizzo= models.CharField(max_length=100, default="")
        telefono= models.CharField(max_length=50, default="")
        livello= models.CharField(max_length=20, default="")
        email= models.CharField(max_length=150, primary_key=True)
        facebook= models.CharField(max_length=200, default="")
        google= models.CharField(max_length=200, default="")
        password= models.CharField(max_length=24, default="")
        autorizzato=models.IntegerField(blank=True, default=0)



class Prenotazioni(models.Model):
    giorno= models.CharField(max_length=50, default="")
    ora=models.CharField(max_length=50, default="")
    note=models.CharField(max_length=300, default="")
    cliente = models.ForeignKey(Clienti, on_delete=models.CASCADE)
    accettata=models.IntegerField(default=0)

class Configurazione(models.Model):
    id = models.AutoField(primary_key=True)
    orariuscitesettimanali = models.CharField(max_length=200) # es. 8-14-18
    giorniuscitesettimanali = models.IntegerField(blank=True, null=True)
    numeropartecipantiperturno= models.IntegerField(blank=True, null=True)
    accettaautomaticamenteprenotazioni= models.IntegerField(blank=True, null=True)