# Generated by Django 5.1.2 on 2024-10-29 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DadosPessoais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperienciaProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('periodo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FormacaoAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('periodo', models.CharField(max_length=50)),
            ],
        ),
    ]
