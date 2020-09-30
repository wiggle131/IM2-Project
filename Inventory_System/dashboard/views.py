from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import CustomerForm, ProductForm
from .models import Customer, Product, Person


def index(request):
    return render(request, 'dashboard/index.html')


def home(request):
    return render(request, 'dashboard/home.html')


class CustomerView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'dashboard/customer.html', {'customer': customers})

    def post(self, request):
        if request.method == 'POST':
            customerid = request.POST.get("customerid")
            delete_product = Customer.objects.filter(
                person_ptr_id=customerid).delete()
            pers = Person.objects.filter(id=customerid).delete()
        return redirect('dashboard-customer')


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "dashboard/product.html", {'product': products})

    def post(self, request):
        if request.method == 'POST':
            pid = request.POST.get("productid")
            delete_product = Product.objects.filter(id=pid).delete()
        return redirect('dashboard-product')


class ProductRegistrationView(View):
    def get(self, request):
        return render(request, 'dashboard/register_prod.html')

    def post(self, request):
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
            profile = request.POST.get("profileImage")
            form = Customer(firstname=fname, middlename=mname, lastname=lname, birthday=bday, gender=gender,
                            status=status, address=address, province=province, zipcode=zipcode, country=country, profile=profile)
            form.save()

            return redirect('dashboard-customer')
        else:
            return HttpResponse('failed')


class ProductUpdateView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'dashboard/register_prod.html', {'product': product})

    def post(self, request, pk):
        if request.method == 'POST':
            pname = request.POST.get("productname")
            brand = request.POST.get("brand")
            color = request.POST.get("color")
            size = request.POST.get("size")
            price = request.POST.get("price")
            no_stock = request.POST.get("no_stocks")
            update_product = Product.objects.filter(id=pk).update(productname=pname, brand=brand, color=color,
                                                                  size=size, price=price, no_stocks=no_stock)
            return redirect('dashboard-product')
        else:
            return HttpResponse('failed')


class CustomerUpdateView(View):
    def get(self, request, pk):
        customer = Customer.objects.get(id=pk)
        return render(request, 'dashboard/register.html', {'customer': customer})

    def post(self, request, pk):
        if request.method == 'POST':
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
            profile = request.POST.get("profileImage")
            update_customer = Customer.objects.filter(person_ptr_id=pk).update(firstname=fname, middlename=mname, lastname=lname, birthday=bday, gender=gender,
                                                                               status=status, address=address, province=province, zipcode=zipcode, country=country, profile=profile)

            return redirect('dashboard-customer')
        else:
            return HttpResponse('failed')
