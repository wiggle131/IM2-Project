from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('dashboard/', views.home, name='dashboard-home'),
    path('dashboard/customer/', views.CustomerView.as_view(),
         name='dashboard-customer'),
    path('dashboard/product/', views.ProductView.as_view(),
         name='dashboard-product'),
    path('dashboard/customer/registration', views.CustomerRegistrationView.as_view(),
         name='dashboard-register'),
    path('dashboard/product/registration', views.ProductRegistrationView.as_view(),
         name='dashboard-register_prod'),
]
