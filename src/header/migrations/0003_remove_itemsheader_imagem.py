# Generated by Django 4.1.1 on 2022-09-15 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0002_itemsheader_imagem_alter_itemsheader_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsheader',
            name='imagem',
        ),
    ]
