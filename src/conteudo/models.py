from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class tipoDeConteudo(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False, verbose_name='Tipo de Contéudo')

    def __str__(self):
        return self.nome

class blocoConteudo(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False)
    local = models.ForeignKey('tipoDeConteudo', on_delete=models.CASCADE)
    conteudo = RichTextField()
    imagem = models.ImageField(upload_to='images')

    def __str__(self):
        return self.nome