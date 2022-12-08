from catalog.models import Catalog, Category, Subcategory
from file import base


def mydb():
    for i in range(0, 706):
        if base[i][0] == None:
            lactose = False
        else:
            lactose = True
        if base[i][1] == None:
            gluten = False
        else:
            gluten = True
        category = base[i][2]
        subcategory = base[i][3]
        name_ru = base[i][4]
        price = int(base[i][5])
        description_ru = base[i][6]
        if base[i][7] == None:
            image = "https://upload.wikimedia.org/wikipedia/commons/9/9a/%D0%9D%D0%B5%D1%82_%D1%84%D0%BE%D1%82%D0%BE.png"
        else:
            image = base[i][7]
        name_eng = base[i][8]
        description_eng = base[i][9]
        Catalog.objects.create(lactose=lactose, gluten=gluten,
                               name_ru=name_ru, price=price,
                               description_ru=description_ru,
                               image=image, name_eng=name_eng,
                               description_eng=description_eng,
                               category=Category.objects.get(title_ru=category),
                               subcategory=Subcategory.objects.get(title_ru=subcategory))
