from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('dashboard/', views.home, name='dashboard-home'),
    path('dashboard/customer/', views.CustomerView.as_view(),
         name='dashboard-customer'),
    path('dashboard/product/', views.ProductView.as_view(),
         name='dashboard-product'),
    path('dashboard/customer/registration', views.CustomerRegistrationView.as_view(),
         name='dashboard-register-customer'),
    path('dashboard/product/registration', views.ProductRegistrationView.as_view(),
         name='dashboard-register_prod'),
    path('dashboard/product/update/<int:pk>/', views.ProductUpdateView.as_view(),
         name='dashboard-update-prod'),
    path('dashboard/customer/update/<int:pk>/', views.CustomerUpdateView.as_view(),
         name='dashboard-update-customer'),
    path('dashboard/orders/', views.OrderView.as_view(),
         name='dashboard-order'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
