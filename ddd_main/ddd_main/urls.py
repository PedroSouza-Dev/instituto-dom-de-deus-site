"""
URL configuration for ddd_main project.

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
from app import views
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('institucional/', views.institucional, name='institucional'),
    path('programas_projetos/', views.programas_projetos, name='programas_projetos'),
    path('transparencia/', views.transparencia, name='transparencia'),
    path('seja_voluntario/', views.seja_voluntario, name='seja_voluntario'),
    path('loja/', views.loja, name='loja'),
    path('patrocinio/', views.patrocinio, name='patrocinio'),
    path('fale_conosco/', views.fale_conosco, name='fale_conosco'),
    path('apoie/', views.apoie, name='apoie'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'app', 'static'))
