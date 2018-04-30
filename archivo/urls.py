from django.conf.urls import url
from .views import ListArchivo, DetailArchivo

urlpatterns = [
    url(r'^archivos/$', ListArchivo.as_view(), name='lista-archivo'),
    url(r'^archivos/(?P<pk>[0-9]+)$', DetailArchivo.as_view(), name='lista-archivo'),

]
