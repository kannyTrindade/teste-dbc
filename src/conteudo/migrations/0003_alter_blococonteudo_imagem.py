# Generated by Django 4.1.1 on 2022-09-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0002_blococonteudo_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blococonteudo',
            name='imagem',
            field=models.ImageField(upload_to='images'),
        ),
    ]
