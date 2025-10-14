from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique = True)
    def __str__(self) :
        return self.name 
class products(models.Model) :
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name = 'products')
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique =True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name


class customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    addresses = models.TextField()
    phone = models.CharField(max_length=20, blank=True)

    __str__(self):
        return self.user.username 


class Cart(models.Model) :
    