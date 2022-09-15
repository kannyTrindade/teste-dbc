from django.db import models

# Create your models here.


class itemsHeader(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False,  verbose_name='Item')
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome