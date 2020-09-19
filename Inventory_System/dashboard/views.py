from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer


def index(request):
    return render(request, 'dashboard/index.html')


def home(request):
    return render(request, 'dashboard/home.html')


class CustomerView(View):
    def get(self, request):
        return render(request, 'dashboard/customer.html')


class ProductView(View):
    def get(self, request):
        return render(request, 'dashboard/product.html')

   # def post(self, request):
        # change register para product here
       # return render(request, 'dashboard/register.html')


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

            return render(request, 'dashboard/customer.html')
        else:
            return HttpResponse('failed')


class ProductRegistrationView(View):
    def get(self, request):
        return render(request, 'dashboard/register_prod.html')

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

            return render(request, 'dashboard/product.html')
        else:
            return HttpResponse('failed')
