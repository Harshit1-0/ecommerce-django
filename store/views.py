from django.shortcuts import render
from .models import Products , Category
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView , ListView
# Create your views here.
def productList(request) :
    products = Products.objects.all()
    cat = Category.objects.all()
  
    print(cat)
    print(products)
  
    return render(request ,'store/productList.html' , {'products' : products , 'cat' : cat} )

class ProductDetail(DetailView) :
    model = Products 
    context_object_name = 'product' 
    template_name = 'store/product_detail.html'

class ProductListByCategory(ListView):
    model = Products
    def get_queryset(self):
        category_slug = self.kwargs.get('slug')  # assuming 'slug' in URL pattern
        if category_slug:
            return Products.objects.filter(category__slug=category_slug)
        else:
            return Products.objects.all()
    # context_object_name = 'products'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['cat'] = Category.objects.all()
        return context
    

    context_object_name = 'products'
    template_name = 'store/productList.html'



