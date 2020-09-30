from django.db import models
from django.utils import timezone


class Education(models.Model):
    elemSchool = models.CharField(max_length=200, blank=True, null=True)
    elemGrade = models.IntegerField(blank=True, null=True)
    elemAwards = models.TextField(blank=True, null=True)
    elemCompleted = models.IntegerField(blank=True, null=True)
    jsSchool = models.CharField(max_length=200, null=True)
    jsGrade = models.IntegerField(blank=True, null=True)
    jsAwards = models.TextField(blank=True, null=True)
    jsCompleted = models.IntegerField(blank=True, null=True)
    srSchool = models.CharField(max_length=200, blank=True, null=True)
    srGrade = models.IntegerField(blank=True, null=True)
    srAwards = models.TextField(blank=True, null=True)
    srCompleted = models.IntegerField(blank=True, null=True)
    collegeSchool = models.CharField(max_length=200, blank=True, null=True)
    collegeGrade = models.IntegerField(blank=True, null=True)
    collegeAwards = models.TextField(blank=True, null=True)
    collegeCompleted = models.IntegerField(blank=True, null=True)
    postSchool = models.CharField(max_length=200, blank=True, null=True)
    postGrade = models.IntegerField(blank=True, null=True)
    postAwards = models.TextField(blank=True, null=True)
    postCompleted = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class Person(Education):
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
    email = models.EmailField(null=True)
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

    class Meta:
        db_table = "Product"
