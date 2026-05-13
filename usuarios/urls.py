from django.contrib import admin
from django.urls import path
from usuarios import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.inicio, name='inicio'),

    path('', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('validaciones/', views.validaciones, name='validaciones'),
    path('notificaciones/', views.notificaciones, name='notificaciones'),
    path('buscar/', views.buscar_operadores, name='buscar'),
    path('editar/<int:id>/', views.editar_operador, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_operador, name='eliminar'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('cerrar/', views.cerrar_sesion, name='cerrar'),
    path('login/', views.login_view, name='login'),
    path('crear-cuenta/', views.registro_usuario, name='registro_usuario'),
]