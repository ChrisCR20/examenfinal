from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas),
    url(r'^compra/nueva/$', views.compra_nueva, name='compra_nueva'),
    ]
