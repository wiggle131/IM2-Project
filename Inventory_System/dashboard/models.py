from django.db import models
from django.utils import timezone


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    address = models.TextField()
    province = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=100)

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

    class Meta:
        db_table = "Product"
