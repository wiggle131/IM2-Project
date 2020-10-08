from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import CustomerForm, ProductForm, OrderForm
from .models import Customer, Product, Person, Order


def index(request):
    return render(request, 'dashboard/index.html')


def home(request):
    customers = Customer.objects.all()[:5]
    products = Product.objects.all()[:5]
    ordercount = Order.objects.all().count()
    customercount = Customer.objects.all().count()
    productcount = Product.objects.all().count()
    context = {
        'customers': customers,
        'products': products,
        'ordercount': ordercount,
        'customercount': customercount,
        'productcount': productcount

    }
    return render(request, 'dashboard/home.html', context)


class CustomerView(View):
    def get(self, request):
        customers = customers = Customer.objects.all()
        products = Product.objects.all()
        orders = Order.objects.all()
        context = {
            'customers': customers,
            'products': products,
            'orders': orders
        }

        return render(request, 'dashboard/customer.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnDelete' in request.POST:
                customerid = request.POST.get("customerid")
                Customer.objects.filter(
                    person_ptr_id=customerid).delete()
                Person.objects.filter(id=customerid).delete()
            elif 'btnOrder' in request.POST:
                customerid = request.POST.get("customerid")
                customer = Customer.objects.filter(
                    person_ptr_id=customerid).get()
                ordered_list = request.POST.getlist('ordered')
                for order in ordered_list:
                    product = Product.objects.filter(id=order).get()
                    product_info_dict = {
                        'customer': customer, 'product': product}
                    Order.objects.create(**product_info_dict)
        return redirect('dashboard-customer')


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "dashboard/product.html", {'product': products})

    def post(self, request):
        if request.method == 'POST':
            if 'btnDelete' in request.POST:
                pid = request.POST.get("productid")
                Product.objects.filter(id=pid).delete()
            elif 'btnFilter' in request.POST:
                if request.POST.get("start_date") and request.POST.get("end_date"):
                    start = request.POST.get("start_date")
                    end = request.POST.get("end_date")
                    products = Product.objects.filter(date_registered__range = (start,end))
                    context = {
                        'product': products,
                        'start_date': start,
                        'end_date': end
                        
                    }
                    return render(request, "dashboard/product.html", context)
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
            email = request.POST.get("email")
            phoneNumber = request.POST.get("phoneNumber")

            form = Customer(firstname=fname, middlename=mname, lastname=lname, birthday=bday, gender=gender,
                            status=status, address=address, province=province, zipcode=zipcode, country=country, profile=profile, email=email, phoneNumber=phoneNumber)

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
            Product.objects.filter(id=pk).update(productname=pname, brand=brand, color=color,
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
            email = request.POST.get("email")
            phoneNumber = request.POST.get("phoneNumber")
            Customer.objects.filter(person_ptr_id=pk).update(firstname=fname, middlename=mname, lastname=lname, birthday=bday, gender=gender,
                                                             status=status, address=address, province=province, zipcode=zipcode, country=country, profile=profile, email=email, phoneNumber=phoneNumber)
            return redirect('dashboard-customer')
        else:
            return HttpResponse('failed')


class OrderView(View):
    def get(self, request):
        orders = Order.objects.all()
        context = {
            'orders': orders,
        }
        return render(request, "dashboard/order.html", context)

    def post(self, request):
        if request.method == 'POST':
            orderid = request.POST.get("orderid")
            if 'btnDelete' in request.POST:
                Order.objects.filter(id=orderid).delete()
            if 'btnConfirm' in request.POST:
                order = Order.objects.filter(id=orderid).get()
                if order.status == 'Pending':
                    order.status = 'Delivered'
                else:
                    order.status = 'Pending'
                order.save()
            return redirect('dashboard-order')
        return redirect('dashboard-order')
