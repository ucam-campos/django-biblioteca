# Generated by Django 2.0.4 on 2018-06-20 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0004_auto_20180605_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='autor',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
