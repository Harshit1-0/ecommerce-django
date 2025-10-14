from django.contrib import admin
from .models import Category, Products, Customer, Cart, CartItem, Order

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
