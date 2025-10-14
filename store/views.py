from django.shortcuts import render
from .models import Products
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
# Create your views here.
def productList(request) :
    products = Products.objects.all()
    print(products)
    return render(request ,store/productList.html , {'product' : products} )

class ProductDetail(DetailView) :
    model = Product 
    context_object_name = 'product' 
    template_name = 'product_detail.html'
