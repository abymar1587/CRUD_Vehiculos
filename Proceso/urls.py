from django.urls import path
from . import views

# las siguientes dos lineas son para configurar la vista de la imagen en el html
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns =[
    path('',views.principal,name='principal'),
    path('vehiculos',views.vehiculos,name='vehiculos'),
    path('vehiculos/crear',views.crear,name='crear'),
    path('vehiculos/editar/<int:id>',views.editar,name='editar'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #configurar la vista de la imagen en el html