from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name='session_list'),
    path('get_students/',views.get_students, name='get_students'),
]
