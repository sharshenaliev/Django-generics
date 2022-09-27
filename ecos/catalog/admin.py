from django.contrib import admin
from .models import Catalog, Category

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'image', 'vision', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category, CategoryAdmin)