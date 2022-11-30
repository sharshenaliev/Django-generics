from django.contrib import admin
from .models import Catalog, Category

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'price', 'image', 'category')
    list_display_links = ('id', 'name_ru')
    search_fields = ('name_ru',)
    list_filter = ('name_ru',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ru')
    list_display_links = ('id', 'title_ru')
    search_fields = ('title_ru',)

admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category, CategoryAdmin)