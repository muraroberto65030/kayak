from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, Http404
from .models import  Clienti, Prenotazioni
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import datetime

def login_register(request):
      return render(request, 'prenotazioni/accesso.html')


def logout_view(request):
    logout(request)
    return render(request, "prenotazioni/accesso.html")


def accesso_utente(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.is_staff:
            # utente admin autenticato
            a = {"msg": "Benvenuto, &nbsp;<b>" + user.username +"</b>", "tipo": "admin"}
        else:
            # utente normale autenticato
            a = {"msg": "Benvenuto, " + user.username, "tipo": "utente"}
    else:
        # utente inesistente
        a = {"msg": "Utente inesistente!"}

    return JsonResponse(a)

def registrazione(request):
    if request.method=="GET":
        #msg = "tuttoOK"
        nome1= request.GET.get('nome', None)
        indirizzo1 = request.GET.get('indirizzo', None)
        eta1 = request.GET.get('eta', None)
        cognome1 = request.GET.get('cognome', None)
        telefono1 = request.GET.get('telefono', None)
        livello1 = request.GET.get('livello', None)
        email1 = request.GET.get('email', None)
        password1 = request.GET.get('password', None)

        objdb = Clienti.objects.create(
            nome=nome1,
            indirizzo=indirizzo1,
            eta=eta1,
            cognome=cognome1,
            telefono=telefono1,
            livello=livello1,
            email=email1,
            password=password1,

        )
        obj={"nome" : objdb.nome}
        msg="Grazie per esserti registrato"

    else:
        obj="a"
        msg="Errore di chiamata"
    pippo={"msg":msg, "obj": obj}
    return JsonResponse(pippo)

def homecliente(request):
    prenotazioni = Prenotazioni.objects.filter(cliente=Clienti.objects.filter(email=request.user.email).first())
    return render(request, 'prenotazioni/homecliente.html', {'prenotazioni': prenotazioni})

def homeadmin(request):
    if request.user.is_staff:
        nuoviclienti = Clienti.objects.filter(autorizzato=0).order_by("nome")
        nuoveprenotazioni=Prenotazioni.objects.filter(giorno__gte=datetime.date.today()).filter(accettata=0).order_by("giorno")
        return render(request, 'prenotazioni/homeadmin.html', {'nuoviclienti': nuoviclienti,"nuoveprenotazioni":nuoveprenotazioni})
    else:
        raise Http404("Operazione non autorizzata! Ci hai provato...")

def accettacliente(request):
    if request.user.is_staff:
        clienteemail=request.POST['email']
        print(clienteemail)
        cliente=Clienti.objects.filter(email=clienteemail).first()
        cliente.autorizzato=1;
        cliente.save()
        User.objects.create_user(cliente.email, cliente.email, cliente.password)
        pippo={"msg":"Utente creato con successo"}
        return JsonResponse(pippo)
    else:
        raise Http404("Operazione non autorizzata! Ci hai provato...")
