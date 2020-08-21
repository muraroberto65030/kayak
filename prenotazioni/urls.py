from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$', views.login_register, name='login_register'),
    url(r'^registrazione', views.registrazione, name='registrazione'),
    url(r'^prenotazioni/login', views.accesso_utente, name='accesso_utente'),
    url(r'^prenotazioni/calendario', views.calendario, name='calendario'),
    url(r'^prenotazioni/lista_clienti', views.lista_clienti, name='lista_clienti'),
    url(r'^prenotazioni/(?P<pk>[0-9]+)/$', views.clienti, name='clienti'),
]