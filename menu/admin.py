from django.contrib import admin

from menu.models import MenuCategory, Menu

# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(Menu)