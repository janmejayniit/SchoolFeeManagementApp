from django.urls import path
from .import views

urlpatterns=[
        path('', views.home, name='student_list'),
        path('add/', views.add_new, name='student_add'),
    ]
