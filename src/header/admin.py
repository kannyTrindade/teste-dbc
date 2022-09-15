from django.contrib import admin
from .models import itemsHeader
# Register your models here.


class items(admin.ModelAdmin):

    list_display = ('nome', 'ativo')

admin.site.register(itemsHeader, items)