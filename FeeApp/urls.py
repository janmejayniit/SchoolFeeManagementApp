from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='fee_list'),
    path('fee_details/<int:invoice>', views.fee_details, name='fee_details'),
]