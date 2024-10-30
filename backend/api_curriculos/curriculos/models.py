from django.db import models

class DadosPessoais(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

class Contato(models.Model):
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)

class ExperienciaProfissional(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
    descricao = models.TextField()

class FormacaoAcademica(models.Model):
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
