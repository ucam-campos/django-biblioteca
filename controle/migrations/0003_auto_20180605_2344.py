# Generated by Django 2.0.4 on 2018-06-05 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_auto_20180605_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='CPF_cliente',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='Tel_cliente',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nome_Cliente',
            new_name='telefone',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='Cargo_Func',
            new_name='Cargo',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='CPF_cliente',
            new_name='Telefone',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='Tel_cliente',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='nome_Funcionario',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='descricao_livro',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='nome_livro',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='quantidade_paginas',
            new_name='quantidade',
        ),
    ]
