from .models import Catalog, Category, Subcategory
from .forms import CustomerForm
from django.views.generic import View, ListView, DetailView, FormView
from django.db.models import Q
from django.shortcuts import redirect, render
import requests

class CatalogList(ListView):
    model = Catalog
    template_name = 'catalog/index.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        context['cart'] = list(map(int, self.request.session.get('cart', ['0'])))
        context['queryset'] = Catalog.objects.filter(id__in=context['cart'])
        context['cart'] = list(map(int, self.request.session.get('cart', [0])))
        context['queryset'] = self.request.session.get('queryset')
        return context


class Search(ListView):
    model = Catalog
    template_name = 'catalog/search.html'
    paginate_by = 24

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
        subcategory = Subcategory.objects.filter(id=self.kwargs['subcategory_id'])
        context['subcategory'] = subcategory
        context['title'] = subcategory.values_list('title_ru', flat=True)[0]
        context['cart'] = list(map(int, self.request.session.get('cart', [])))
        context['queryset'] = Catalog.objects.filter(id__in=context['cart'])
        context['cart'] = list(map(int, self.request.session.get('cart', [0])))
        context['queryset'] = self.request.session['queryset']
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
        context['cart'] = list(map(int, self.request.session.get('cart', ['0'])))
        context['queryset'] = Catalog.objects.filter(id__in=context['cart'])
        context['cart'] = list(map(int, self.request.session.get('cart', [0])))
        context['queryset'] = self.request.session['queryset']
        return context


class Cart(ListView):
    template_name = 'catalog/cart.html'

    def get_queryset(self):
         return self.request.session['queryset']

    def post(self, request):
        product = self.request.POST.get('pk')
        cart = self.request.session.get('cart', ['0'])
        if product in cart:
            cart.remove(product)
        else:
            cart.append(product)
        self.request.session['cart'] = cart
        self.request.session['queryset'] = Catalog.objects.filter(id__in=cart)
        if product == '0':
            return redirect('cart')
        else:
            return redirect(request.META.get('HTTP_REFERER'))

class Order(FormView):
    template_name = 'catalog/order.html'
    form_class = CustomerForm
    success_url = '/success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchase'] = self.request.session['purchase']
        if context['purchase'] < 3000:
            context['delivery'] = 200
        else:
            context['delivery'] = 0
        context['total'] = context['purchase'] + context['delivery']
        return context

    def post(self, request):
        products = self.request.session['queryset']
        quantity = self.request.POST.getlist('quantity')
        purchase = 0
        for i in range(0, len(quantity)):
            purchase += int(quantity[i]) * products.values_list('price', flat=True)[i]
        self.request.session['purchase'] = purchase
        self.request.session['quantity'] = quantity
        return redirect('order')


class Success(View):
    template_name = 'catalog/success.html'

    def get(self, request):
        message = 'Ваш заказ принят!'
        return render(request, template_name='catalog/success.html', context={'message': message})

    def post(self, request):
        form = CustomerForm(request.POST)
        order = ""
        if form.is_valid():
            for i in range(0, len(self.request.session['quantity'])):
                order += str(self.request.session['quantity'][i]) + ' штук ' + str(self.request.session['queryset'].values_list('name_ru', flat=True)[i])

            TOKEN = '1105029676:AAFouNcKmqpe5MOJ5neACqwZD5w7pgLjFMU'
            chat_id = '826921885'

            message = f"Номер телефона: {form.cleaned_data['phone']}. " \
                      f"Имя клиента: {form.cleaned_data['name']}. " \
                      f"Адрес: {form.cleaned_data['address']}. " \
                      f"Стоимость: {request.session['purchase']} сом " \
                      f'Заказ: {order}.'

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

            print(requests.get(url).json())
            del self.request.session['cart']
            self.request.session.modified = True
        return redirect('success')
