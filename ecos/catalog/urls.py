from django.urls import path
from .views import *

urlpatterns = [
    path('', CatalogList.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('pricelow/', Ordering.as_view(), name='pricelow'),
    path('lactose/', Lactose.as_view(), name='lactose'),
    path('gluten/', Gluten.as_view(), name='gluten'),
    path('category/<int:subcategory_id>/', GetCategory.as_view(), name='category'),
    path('category_pricelow/<int:subcategory_id>/', OrderingCategory.as_view(), name='category_pricelow'),
    path('category_lactose/<int:subcategory_id>/', LactoseCategory.as_view(), name='category_lactose'),
    path('category_gluten/<int:subcategory_id>/', GlutenCategory.as_view(), name='category_gluten'),
    path('product/<int:pk>/', ShowProduct.as_view(), name='product'),
    path('cart/', Cart.as_view(), name='cart'),
    path('order/', Order.as_view(), name='order'),
    path('success/', Success.as_view(), name='success')
]
