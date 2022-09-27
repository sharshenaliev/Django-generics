from catalog.models import Catalog, Category
from file import base


def mydb():
    for i in range(26, 350):
        if base[i][3] == None:
            img = "https://upload.wikimedia.org/wikipedia/commons/9/9a/%D0%9D%D0%B5%D1%82_%D1%84%D0%BE%D1%82%D0%BE.png"
        else:
            img = base[i][3]
        Catalog.objects.create(title=base[i][0], price=int(base[i][1]), image=img, category=Category.objects.get(title=base[i][2]))
