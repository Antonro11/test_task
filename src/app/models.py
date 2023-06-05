from django.db import models


# Create your models here.


class Shop(models.Model):
    shop_name = models.CharField(max_length=40)
    products = models.ManyToManyField(to="app.Product", related_name="shops", null=True)
    logo = models.ImageField(upload_to="static/logo", blank=True)

    def __str__(self):
        return f"{self.shop_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to="static/product_image", blank=True)
    price = models.IntegerField()
    shop = models.CharField(max_length=40, null=True)

    def __str__(self):
        return f"{self.product_name}"


class ShopCard(models.Model):
    balance = models.IntegerField(default=20)
    products = models.CharField(max_length=200, default="[]")


class ShopIndexAnon(models.Model):
    index_shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True,null=True)