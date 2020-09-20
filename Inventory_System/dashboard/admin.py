from django.contrib import admin
from .models import Person, Customer, Product

# Register your models here.
admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Product)
