# Generated by Django 4.1.1 on 2022-09-14 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('link', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='link',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
