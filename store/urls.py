from django.urls import path 
from . import views
urlpatterns = [
    path('product/' , views.productList , name ='productList' ) ,
    path('product/<int:pk>' , views.ProductDetail.as_view() , name = 'detailView') ,
    path('product/category/<slug:slug>' , views.ProductListByCategory.as_view() , name='productByCat'),
    path('cart/add/<int:pk>/', views.addToCart , name = 'addToCart'),
    path('cart' , views.cart , name = 'cart')
]
