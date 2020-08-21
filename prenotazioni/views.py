from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from .models import  Clienti, Prenotazioni
from django.contrib.auth import authenticate, login, logout

def login_register(request):
      return render(request, 'prenotazioni/accesso.html')
    #return render(request, "prenotazioni/login.html")


def logout_view(request):
    logout(request)
    return render(request, "prenotazioni/login.html")


def accesso_utente(request):
    username = request.POST['loginemail']
    password = request.POST['loginpassword']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.is_staff:
            # utente admin autenticato
            a = {"msg": "Benvenuto:!&nbsp;<b>" + user.username +"</b>"}
        else:
            # utente normale autenticato
            a = {"msg": "Benvenuto:!" + user.username}
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

def calendario(request):
    return render(request, "prenotazioni/calendario.html")

def clienti(request, id):
    return render(request, "prenotazioni/clienti.html", {'object': Clienti.objects.get(pk=id)})

def lista_clienti(request):
    clientis = Clienti.objects.order_by("nome")
    return render(request, 'prenotazioni/lista_clienti.html', {'clientis': clientis})
