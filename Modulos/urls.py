
from django.contrib import admin
from django.conf import urls
from Modulos.models import registro1
from django.urls.conf import path, include
from django.conf import settings
from django.urls import re_path
from . import views
from django.conf.urls.static import static

urlpatterns=[
     path('admin/',admin.site.urls),
     path('', include('Modulos.urls')),
     path('accounts/', include('django.contrib.auth.urls'))      
]


urlpatterns = [
     re_path( r'^$', views.index2, name="index2"), # funcion re_path remplaza url
     re_path( r'^login.html/$', views.login, name="login"),
     re_path( r'^registro.html/$', views.registro, name="registro_views"),
     
]
