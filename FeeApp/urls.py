from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='fee_list'),
    path('fee_details/<int:invoice>', views.fee_details, name='fee_details'),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
    path('get_fee/', views.get_fee, name='get_fee'),
]