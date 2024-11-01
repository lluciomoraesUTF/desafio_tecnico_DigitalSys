from rest_framework import generics
from .models import DadosPessoais, Habilidades, Experiencia, Educacao  # Certifique-se de que os modelos Experiencia e Educacao estão definidos
from .serializers import DadosPessoaisSerializer, HabilidadesSerializer, ExperienciaSerializer, EducacaoSerializer  # Certifique-se de que os serializers correspondentes estão definidos

class DadosPessoaisListCreateView(generics.ListCreateAPIView):
    queryset = DadosPessoais.objects.all()
    serializer_class = DadosPessoaisSerializer

class DadosPessoaisRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DadosPessoais.objects.all()
    serializer_class = DadosPessoaisSerializer

class HabilidadesListCreateView(generics.ListCreateAPIView):
    queryset = Habilidades.objects.all()
    serializer_class = HabilidadesSerializer

class HabilidadesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habilidades.objects.all()
    serializer_class = HabilidadesSerializer

class ExperienciaListCreateView(generics.ListCreateAPIView):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

class ExperienciaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

class EducacaoListCreateView(generics.ListCreateAPIView):
    queryset = Educacao.objects.all()
    serializer_class = EducacaoSerializer

class EducacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Educacao.objects.all()
    serializer_class = EducacaoSerializer
