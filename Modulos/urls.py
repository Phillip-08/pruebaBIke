
from django.contrib import admin
from django.conf import urls
from Modulos.models import registro1
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import re_path
from . import views
from django.conf.urls.static import static


urlpatterns = [
     re_path( r'^$', views.index2, name="index2"), # funcion re_path remplaza url
     re_path( r'^login.html/$', views.login, name="login"),
     re_path( r'^registrar.html/$', views.registrar, name="registrar"), 
     re_path( r'^Planes.html/$', views.Planes, name="Planes"),
     re_path( r'^nosotros.html/$', views.nosotros, name="nosotros"),
     re_path( r'^contacto.html/$', views.contacto, name="contacto"),
     re_path( r'^Mapa.html/$', views.Mapa, name="Mapa"),

     path('reset_password/', auth_views.PasswordResetView.as_view(template_name="Modulos/templates/password_reset.html"), name="reset_password"), 
     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="Modulos/password_reset_done.html"), name="password_reset_done"),
     path('reset/<uidb64><token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
     path('reset_password_complete/', auth_views.PasswordResetView.as_view(),name="password_reset_complete"),
]
