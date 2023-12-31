"""
URL configuration for modelDemo1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejercicioApp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu_principal, name='menu_principal'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/actualizar/<int:id_producto>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/eliminar/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
]
