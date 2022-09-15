from django.db import models

# Create your models here.



class SubMenu(models.Model):
    titulo = models.CharField(max_length=70, blank=False, null=False)
    link = models.CharField(max_length=300, blank=False, null=False)
    novo = models.BooleanField()

    def __str__(self):
        return self.titulo

class Menu(models.Model):
    titulo = models.CharField(max_length=70, blank=False, null=False)
    link = models.CharField(max_length=300, blank=True, null=True)
    subMenus = models.ManyToManyField(SubMenu, blank=True)

    def __str__(self):
        return self.titulo