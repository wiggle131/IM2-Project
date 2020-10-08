from django.db import models
from django.utils import timezone


class Person(models.Model):
    firstname = models.CharField(max_length=100, blank=True, null=True)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.IntegerField(null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phoneNumber = models.IntegerField(null=True)

    class Meta:
        db_table = "Person"


class Customer(Person):
    profile = models.ImageField(null=True, blank=True, upload_to="images/")
    date_registered = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "Customer"


class Product(models.Model):
    productname = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    size = models.FloatField()
    price = models.FloatField()
    no_stocks = models.IntegerField()
    date_registered = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "Product"


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=15, default='Pending')
    cost = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        db_table = "Order"
