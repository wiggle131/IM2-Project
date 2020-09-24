from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import CustomerForm, ProductForm
from .models import Customer, Product


def index(request):
    return render(request, 'dashboard/index.html')


def home(request):
    return render(request, 'dashboard/home.html')


class CustomerView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'dashboard/customer.html',{'customer': customers})


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "dashboard/product.html", {'product': products})


class ProductRegistrationView(View):
    def get(self, request):
        return render(request, 'dashboard/register_prod.html')

    def post(self, request):
        print('yow')
        form = ProductForm(request.POST)
        if form.is_valid():
            pname = request.POST.get("productname")
            brand = request.POST.get("brand")
            color = request.POST.get("color")
            size = request.POST.get("size")
            price = request.POST.get("price")
            no_stock = request.POST.get("no_stocks")
            form = Product(productname=pname, brand=brand, color=color,
                           size=size, price=price, no_stocks=no_stock)
            form.save()

            return redirect('dashboard-product')
        else:
            return HttpResponse('failed')


class CustomerRegistrationView(View):
    def get(self, request):
        return render(request, 'dashboard/register.html')

    def post(self, request):
        print('yow')
        form = CustomerForm(request.POST)
        if form.is_valid():
            fname = request.POST.get("firstname")
            mname = request.POST.get("middlename")
            lname = request.POST.get("lastname")
            bday = request.POST.get("birthday")
            gender = request.POST.get("gender")
            status = request.POST.get("status")
            address = request.POST.get("address")
            province = request.POST.get("province")
            zipcode = request.POST.get("zipcode")
            country = request.POST.get("country")
            form = Customer(firstname=fname, middlename=mname, lastname=lname, birthday=bday, gender=gender,
                            status=status, address=address, province=province, zipcode=zipcode, country=country)
            form.save()

            return redirect('dashboard-customer')
        else:
            return HttpResponse('failed')
