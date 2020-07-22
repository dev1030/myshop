from django.db import models
from django.db import connection

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

class Products(models.Model):
    Product_Name = models.CharField(max_length=100)
    price = models.FloatField()
    Description = models.TextField()
    ctg = models.ForeignKey(categorie, on_delete=models.CASCADE,blank = False,  default=1)
    sub_category = models.ForeignKey(sub_categorie, on_delete=models.CASCADE,default=1)
