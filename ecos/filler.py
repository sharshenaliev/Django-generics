from catalog.models import Category, Subcategory
from categories import subcats


def mydb():
    for c in subcats:
        Subcategory.objects.create(category=Category.objects.get(pk=c[0]), title_ru=c[1], title_eng=c[2])
        
