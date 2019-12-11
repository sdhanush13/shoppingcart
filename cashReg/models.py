from django.db import models
from django.urls import reverse


# Create your models here.
class AddProduct(models.Model):
    Product_Name = models.CharField(max_length=100)
    Category_Name = models.CharField(max_length=50)
    Price = models.FloatField(max_length=20)
    Quantity = models.IntegerField()

    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])

    def __str__(self):
        return self.Product_Name


class Cart(models.Model):
    products = models.ManyToManyField(AddProduct, null=True, blank=True)
    total = models.FloatField(max_length=20)

    def __unicode__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])
