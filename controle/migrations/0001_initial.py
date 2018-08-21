# Generated by Django 2.0.4 on 2018-05-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_text', models.CharField(max_length=255)),
                ('CPF_cliente', models.IntegerField(default=0)),
                ('Tel_cliente', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_funcionario', models.IntegerField(default=0)),
                ('nome_text', models.CharField(max_length=255)),
                ('CPF_cliente', models.IntegerField(default=0)),
                ('Tel_cliente', models.IntegerField(default=0)),
                ('Cargo_Func', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_livro', models.IntegerField(default=0)),
                ('nome_livro', models.CharField(max_length=255)),
                ('descricao_livro', models.CharField(max_length=200)),
                ('quantidade_paginas', models.IntegerField(default=0)),
            ],
        ),
    ]
