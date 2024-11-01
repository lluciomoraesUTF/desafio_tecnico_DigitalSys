"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from api_curriculos.views import (
    DadosPessoaisListCreateView,
    DadosPessoaisRetrieveUpdateDestroyView,
    HabilidadesListCreateView,
    HabilidadesRetrieveUpdateDestroyView,
    ExperienciaListCreateView,
    ExperienciaRetrieveUpdateDestroyView,
    EducacaoListCreateView,
    EducacaoRetrieveUpdateDestroyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_curriculos/', include('api_curriculos.urls')),  # Inclui as URLs do app api_curriculos
    path('dadospessoais/', DadosPessoaisListCreateView.as_view(), name='dadospessoais'),
    path('habilidades/', HabilidadesListCreateView.as_view(), name='habilidades'),
    path('experiencias/', ExperienciaListCreateView.as_view(), name='experiencias'),
    path('educacoes/', EducacaoListCreateView.as_view(), name='educacoes'),
    path('dadospessoais/<int:pk>/', DadosPessoaisRetrieveUpdateDestroyView.as_view(), name='dadospessoais-detail'),
    path('habilidades/<int:pk>/', HabilidadesRetrieveUpdateDestroyView.as_view(), name='habilidades-detail'),
    path('experiencias/<int:pk>/', ExperienciaRetrieveUpdateDestroyView.as_view(), name='experiencias-detail'),
    path('educacoes/<int:pk>/', EducacaoRetrieveUpdateDestroyView.as_view(), name='educacoes-detail'),

]

