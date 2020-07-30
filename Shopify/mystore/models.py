from django.db import models
from django.db import connection
from django.contrib.auth.models import User

# Create your models here.

class categorie(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class sub_categorie(models.Model):
    sub_name = models.CharField(max_length=100)
    catagory_name = models.ForeignKey(categorie, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.sub_name

class brand(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class Products(models.Model):
    Product_Name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img', null = False, default=1)
    price = models.FloatField()
    Description = models.TextField()
    ctg = models.ForeignKey(categorie, on_delete=models.CASCADE, blank=False, default=1)
    sub_category = models.ForeignKey(sub_categorie, on_delete=models.CASCADE, null=True, blank=True)
    brand_name = models.ForeignKey(brand, on_delete=models.CASCADE, null= True, blank = True)

    def __str__(self):
        return self.Product_Name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    Order_date = models.DateTimeField(auto_now_add=True)
    complate = models.BooleanField(default=False, null=True, blank=False)

    @property
    def get_cart_total(self):
        OrderItems = self.orderitem_set.all()
        total = sum(item.get_total for item in OrderItems)
        return total

class OrderItem(models.Model):
    Product = models.ForeignKey(Products, on_delete=models.CASCADE,blank = True, null = True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE,blank = True, null = True)
    Quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.Product.price * self.Quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE,blank = True, null = True)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
