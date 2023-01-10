"""djangoProjectof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1.views import index_page
from app1.views import home_page
from app1.views import demanda_page
from app1.views import geografia_page
from app1.views import habilidades_page
from app1.views import vacantes_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_page),
    path('newjob',home_page),
    path('demand',demanda_page),
    path('geography', geografia_page),
    path('skill', habilidades_page),
    path('vacancy', vacantes_page),
]
