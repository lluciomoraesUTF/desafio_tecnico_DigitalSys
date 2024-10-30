from rest_framework import viewsets
from .models import DadosPessoais, ExperienciaProfissional, FormacaoAcademica
from .serializers import DadosPessoaisSerializer, ExperienciaProfissionalSerializer, FormacaoAcademicaSerializer

class DadosPessoaisViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all()
    serializer_class = DadosPessoaisSerializer

class ExperienciaProfissionalViewSet(viewsets.ModelViewSet):
    queryset = ExperienciaProfissional.objects.all()
    serializer_class = ExperienciaProfissionalSerializer

class FormacaoAcademicaViewSet(viewsets.ModelViewSet):
    queryset = FormacaoAcademica.objects.all()
    serializer_class = FormacaoAcademicaSerializer
