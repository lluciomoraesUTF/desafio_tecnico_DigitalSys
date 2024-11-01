from django.db import models

class DadosPessoais(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    celular = models.CharField(max_length=15)
    endereco = models.TextField()
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Habilidades(models.Model):
    habilidade = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)  # Exemplos: 'Iniciante', 'Intermediário', 'Avançado'
    dados_pessoais = models.ForeignKey(DadosPessoais, related_name='habilidades', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.habilidade} - {self.nivel}"
class Experiencia(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    dados_pessoais = models.ForeignKey(DadosPessoais, related_name='experiencias', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.habilidade} - {self.nivel}"

from django.db import models

class Educacao(models.Model):
    STATUS_CHOICES = [
        ('Concluído', 'Concluído'),
        ('Em andamento', 'Em andamento'),
        ('Trancado', 'Trancado'),
    ]

    instituicao = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    periodo = models.CharField(max_length=100, blank=True, null=True)  # Permitir vazio se não estiver em andamento

    def __str__(self):
        return f"{self.curso} - {self.instituicao}"

