import re
from rest_framework import serializers
from .models import DadosPessoais, ExperienciaProfissional, FormacaoAcademica

class DadosPessoaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = ['nome', 'email', 'telefone']

    def validate_nome(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return value

    def validate_email(self, value):
        # Validação básica de formato de email
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, value):
            raise serializers.ValidationError("Insira um endereço de email válido.")
        return value

    def validate_telefone(self, value):
        # Validação: apenas dígitos e comprimento de 10 ou 11 caracteres
        if not value.isdigit() or len(value) not in [10, 11]:
            raise serializers.ValidationError("O telefone deve conter apenas números e ter 10 ou 11 dígitos.")
        return value


class ExperienciaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaProfissional
        fields = ['empresa', 'cargo', 'data_inicio', 'data_fim', 'descricao']

    def validate_empresa(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("O nome da empresa deve ter pelo menos 2 caracteres.")
        return value

    def validate_cargo(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("O cargo deve ter pelo menos 2 caracteres.")
        return value

    def validate(self, data):
        # Validação: data de início deve ser anterior à data de término
        if data['data_fim'] and data['data_inicio'] > data['data_fim']:
            raise serializers.ValidationError("A data de início não pode ser posterior à data de término.")
        return data


class FormacaoAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormacaoAcademica
        fields = ['instituicao', 'curso', 'data_inicio', 'data_fim']

    def validate_instituicao(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("O nome da instituição deve ter pelo menos 2 caracteres.")
        return value

    def validate_curso(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome do curso deve ter pelo menos 3 caracteres.")
        return value

    def validate(self, data):
        # Validação: data de início deve ser anterior à data de término
        if data['data_fim'] and data['data_inicio'] > data['data_fim']:
            raise serializers.ValidationError("A data de início não pode ser posterior à data de término.")
        return data
