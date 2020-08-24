from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$', views.login_register, name='login_register'),
    url(r'^registrazione', views.registrazione, name='registrazione'),
    url(r'^prenotazioni/login', views.accesso_utente, name='accesso_utente'),
    url(r'^prenotazioni/logout', views.logout_view, name='logout'),
    url(r'^prenotazioni/homeadmin', views.homeadmin, name='homeadmin'),
    url(r'^prenotazioni/homecliente', views.homecliente, name='homecliente'),
    url(r'^prenotazioni/accettacliente', views.accettacliente, name='accettacliente'),
]