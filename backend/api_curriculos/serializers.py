from rest_framework import serializers
from .models import DadosPessoais, Habilidades, Experiencia, Educacao

class HabilidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidades
        fields = ['id', 'habilidade', 'nivel']

class DadosPessoaisSerializer(serializers.ModelSerializer):
    habilidades = HabilidadesSerializer(many=True, required=False)

    class Meta:
        model = DadosPessoais
        fields = ['id', 'nome', 'sobrenome', 'data_nascimento', 'email', 'celular', 'endereco', 'habilidades']

    def create(self, validated_data):
        habilidades_data = validated_data.pop('habilidades', [])
        dados_pessoais = DadosPessoais.objects.create(**validated_data)
        for habilidade_data in habilidades_data:
            Habilidades.objects.create(dados_pessoais=dados_pessoais, **habilidade_data)
        return dados_pessoais

    def update(self, instance, validated_data):
        habilidades_data = validated_data.pop('habilidades', [])
        instance.nome = validated_data.get('nome', instance.nome)
        instance.sobrenome = validated_data.get('sobrenome', instance.sobrenome)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
        instance.email = validated_data.get('email', instance.email)
        instance.celular = validated_data.get('celular', instance.celular)
        instance.endereco = validated_data.get('endereco', instance.endereco)
        instance.save()

        # Atualizando habilidades
        for habilidade_data in habilidades_data:
            habilidade_id = habilidade_data.get('id', None)
            if habilidade_id:
                habilidade = Habilidades.objects.get(id=habilidade_id, dados_pessoais=instance)
                habilidade.habilidade = habilidade_data.get('habilidade', habilidade.habilidade)
                habilidade.nivel = habilidade_data.get('nivel', habilidade.nivel)
                habilidade.save()
            else:
                Habilidades.objects.create(dados_pessoais=instance, **habilidade_data)

        return instance

class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia
        fields = ['id', 'cargo', 'empresa', 'data_inicio', 'data_fim']

    def create(self, validated_data):
        return Experiencia.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cargo = validated_data.get('cargo', instance.cargo)
        instance.empresa = validated_data.get('empresa', instance.empresa)
        instance.data_inicio = validated_data.get('data_inicio', instance.data_inicio)
        instance.data_fim = validated_data.get('data_fim', instance.data_fim)
        instance.save()
        return instance

class EducacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educacao
        fields = ['id', 'instituicao', 'curso', 'status', 'periodo']


    def create(self, validated_data):
        return Educacao.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.instituicao = validated_data.get('instituicao', instance.instituicao)
        instance.grau = validated_data.get('grau', instance.grau)
        instance.data_inicio = validated_data.get('data_inicio', instance.data_inicio)
        instance.data_fim = validated_data.get('data_fim', instance.data_fim)
        instance.save()
        return instance
