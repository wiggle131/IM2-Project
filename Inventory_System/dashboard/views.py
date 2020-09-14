from django.shortcuts import render
from django.views.generic import View


def index(request):
    return render(request, 'dashboard/index.html')


def home(request):
    return render(request, 'dashboard/home.html')


class CustomerView(View):
    def get(self, request):
        return render(request, 'dashboard/customer.html')

    def post(self, request):
        return render(request, 'dashboard/register.html')


class ProductView(View):
    def get(self, request):
        return render(request, 'dashboard/product.html')

    def post(self, request):
        # change register para product here
        return render(request, 'dashboard/register.html')


def register(request):
    return render(request, 'dashboard/register.html')


def register2(request):
    return render(request, 'dashboard/registration2.html')
