from django.urls import path 
from . import views
urlpatterns = [
    path('productlist/' , views.productList , name ='productList' ) ,
    path('product/<int:pk>' , views.ProductDetail.as_view() , name = 'detailView')
]
