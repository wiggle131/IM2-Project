from django.forms import ModelForm
from .models import Customer, Product, Order


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = ('firstname', 'lastname')


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('productname',)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
