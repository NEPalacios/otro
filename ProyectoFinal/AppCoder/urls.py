from django.urls import path
from . import views


app_name = 'productos'

urlpatterns = [
    path('', views.home, name='index'),
    path('productos/', views.consultar, name="consultar"),
    path('guardar/', views.guardar, name="guardar"),   
    #ruta/id de tabla
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('detalle/<int:id>', views.detalle, name='detalle'),

]