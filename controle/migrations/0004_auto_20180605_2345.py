# Generated by Django 2.0.4 on 2018-06-05 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0003_auto_20180605_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='Cargo',
            new_name='cargo',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='Telefone',
            new_name='telefone',
        ),
    ]
