from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('dashboard/', views.home, name='dashboard-home'),
    path('dashboard/customer/', views.CustomerView.as_view(),
         name='dashboard-customer'),
    path('dashboard/product/', views.ProductView.as_view(),
         name='dashboard-product'),
    path('dashboard/register/', views.register, name='dashboard-register'),
    path('dashboard/register2/', views.register2, name='dashboard-register2'),
]
