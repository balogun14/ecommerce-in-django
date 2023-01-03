from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


user = get_user_model()



class Category(models.Model):
    name = models.CharField(null=True, blank=True, max_length=25,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'




class Product(models.Model):
    title = models.CharField(null=True, blank=True, max_length=25,)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='static/media', null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(null=True, blank=True, max_length=25,)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Cart(models.Model):
    customer = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    transactionId = models.CharField(
        max_length=25, null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.customer)
    


class OrderProduct(models.Model):
    customers = models.ForeignKey(user, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    delivered = models.BooleanField(default=False)
    trackingId = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return str(self.product)
