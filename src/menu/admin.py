from django.contrib import admin
from .models import Menu, SubMenu
# Register your models here.

class menuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'submenus')

    def submenus(self, obj):
        return " / ".join([a.titulo for a in obj.subMenus.all()])

class submenuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link', 'novo')


admin.site.register(Menu, menuAdmin)
admin.site.register(SubMenu, submenuAdmin)