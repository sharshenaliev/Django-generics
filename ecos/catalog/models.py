from django.db import models


class Catalog(models.Model):
    name_ru = models.CharField(max_length=150)
    name_eng = models.CharField(max_length=150)
    price = models.IntegerField(blank=True)
    image = models.CharField(max_length=150, blank=True)
    description_ru = models.TextField()
    description_eng = models.TextField()
    lactose = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    title_ru = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title_ru = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
