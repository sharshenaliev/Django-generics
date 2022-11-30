from .models import Catalog, Category, Subcategory
from django.views.generic import ListView, DetailView
from django.db.models import Q


class CatalogList(ListView):
    model = Catalog
    template_name = 'catalog/index.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        return context


class Search(ListView):
    model = Catalog
    template_name = 'catalog/search.html'
    paginate_by = 15

    def get_queryset(self):
         return Catalog.objects.filter(Q(description_ru__icontains=self.request.GET.get('search')) |
                                       Q(name_ru__icontains=self.request.GET.get('search')) |
                                       Q(name_eng__icontains=self.request.GET.get('search')) |
                                       Q(description_eng__icontains=self.request.GET.get('search')) |
                                       Q(description_ru__icontains=self.request.GET.get('search').lower()) |
                                       Q(name_ru__icontains=self.request.GET.get('search').lower()) |
                                       Q(name_eng__icontains=self.request.GET.get('search').lower()) |
                                       Q(description_eng__icontains=self.request.GET.get('search').lower()) |
                                       Q(description_ru__icontains=self.request.GET.get('search').capitalize()) |
                                       Q(name_ru__icontains=self.request.GET.get('search').capitalize()) |
                                       Q(name_eng__icontains=self.request.GET.get('search').capitalize()) |
                                       Q(description_eng__icontains=self.request.GET.get('search').capitalize())
                                       )

class Ordering(CatalogList):
    ordering = ['price']


class Lactose(CatalogList):

     def get_queryset(self):
        return Catalog.objects.filter(lactose=True)


class Gluten(CatalogList):

    def get_queryset(self):
        return Catalog.objects.filter(gluten=True)


class GetCategory(CatalogList):
    template_name = 'catalog/category.html'

    def get_queryset(self):
        return Catalog.objects.filter(subcategory_id=self.kwargs['subcategory_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        context['subcategory'] = Subcategory.objects.filter(id=self.kwargs['subcategory_id'])
        return context


class OrderingCategory(GetCategory):

    def get_queryset(self):
        return Catalog.objects.filter(subcategory_id=self.kwargs['subcategory_id']).order_by('price')


class LactoseCategory(GetCategory):

    def get_queryset(self):
        return Catalog.objects.filter(subcategory_id=self.kwargs['subcategory_id'], lactose=True)


class GlutenCategory(GetCategory):

    def get_queryset(self):
        return Catalog.objects.filter(subcategory_id=self.kwargs['subcategory_id'], gluten=True)


class ShowProduct(DetailView):
    model = Catalog
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        return context