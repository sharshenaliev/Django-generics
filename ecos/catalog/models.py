from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    image = models.CharField(max_length=150, blank=True)
    vision = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'