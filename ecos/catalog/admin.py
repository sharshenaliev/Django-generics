from django.contrib import admin
from .models import Catalog

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'price', 'image', 'category', 'subcategory', )
    list_display_links = ('id', 'name_ru')
    search_fields = ('name_ru',)
    list_filter = ('subcategory',)


admin.site.register(Catalog, CatalogAdmin)
