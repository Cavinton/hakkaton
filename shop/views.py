from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet


# Create your views here.

# from cart.forms import CartAddProductForm
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product/detail.html', {'product': product,
#                                                         'cart_product_form': cart_product_form})
