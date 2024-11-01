from django.urls import path
from .views import (
    DadosPessoaisListCreateView,
    DadosPessoaisRetrieveUpdateDestroyView,
    HabilidadesListCreateView,
    HabilidadesRetrieveUpdateDestroyView,
    ExperienciaListCreateView,
    ExperienciaRetrieveUpdateDestroyView,
    EducacaoListCreateView,
    EducacaoRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('dadospessoais/', DadosPessoaisListCreateView.as_view(), name='dadospessoais'),
    path('habilidades/', HabilidadesListCreateView.as_view(), name='habilidades'),
    path('experiencias/', ExperienciaListCreateView.as_view(), name='experiencias'),
    path('educacoes/', EducacaoListCreateView.as_view(), name='educacoes'),
    path('dadospessoais/<int:pk>/', DadosPessoaisRetrieveUpdateDestroyView.as_view(), name='dadospessoais-detail'),
    path('habilidades/<int:pk>/', HabilidadesRetrieveUpdateDestroyView.as_view(), name='habilidades-detail'),
    path('experiencias/<int:pk>/', ExperienciaRetrieveUpdateDestroyView.as_view(), name='experiencias-detail'),
    path('educacoes/<int:pk>/', EducacaoRetrieveUpdateDestroyView.as_view(), name='educacoes-detail'),
]
